import random
import datetime
import prettytable  # пакет для таблицы
import matplotlib.pyplot as plt  # библиотека для графика


def BubbleSort(A):  # сортировка пузырьком
    for i in range(len(A)):
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                a = A[j]
                A[j] = A[j + 1]
                A[j + 1] = a


def SelectionSort(A):  # сортировка выбором
    for i in range(len(A) - 1):
        k = i
        for j in range(i + 1, len(A)):
            if A[j] < A[k]:
                k = j
        A[i], A[k] = A[k], A[i]


def InsertionSort(A):  # сортировка вставками
    for i in range(len(A) - 1):
        j = i + 1
        while j > 0 and A[j] > A[j - 1]:
            A[j], A[j - 1] = A[j - 1], A[j]
            j -= 1


def MergeSort(A):  # сортировка слиянием
    if len(A) > 1:
        mid = len(A) // 2
        L = A[: mid]
        R = A[mid:]
        MergeSort(L)
        MergeSort(R)
        l = r = i = 0
        while l < len(L) and r < len(R):
            if L[l] < R[r]:
                A[i] = L[l]
                l += 1
            else:
                A[i] = R[r]
                r += 1
            i += 1
        while l < len(L):
            A[i] = L[l]
            i += 1
            l += 1
        while r < len(R):
            A[i] = R[r]
            i += 1
            r += 1


table = prettytable.PrettyTable(["Размер списка", "Время пузырька", "Время выбора", "Время вставки", "Время слияния"])
x = []
y1 = []
y2 = []
y3 = []
y4 = []

for N in range(1000, 5001, 1000):
    x.append(N)
    min = 1
    max = N
    A = []
    for i in range(N):
        A.append(int(round(random.random() * (max - min) + min)))
    B = A.copy()
    C = A.copy()
    D = A.copy()
    print("Список до сортировки:")
    print(A)
    print("-------------------------------------------------------------------------------")
    t1 = datetime.datetime.now()
    BubbleSort(A)
    t2 = datetime.datetime.now()
    print(A)
    y1.append((t2 - t1).total_seconds())
    print("Пузырьковая сортировка   " + str(N) + "   заняла   " + str((t2 - t1).total_seconds()) + "c")

    t3 = datetime.datetime.now()
    SelectionSort(B)
    t4 = datetime.datetime.now()
    print(B)
    y2.append((t4 - t3).total_seconds())
    print("Выбором   " + str(N) + "   заняла   " + str((t4 - t3).total_seconds()) + "c")

    t5 = datetime.datetime.now()
    InsertionSort(C)
    t6 = datetime.datetime.now()
    print(C)
    y3.append((t6 - t5).total_seconds())
    print("Вставками   " + str(N) + "   заняла   " + str((t6 - t5).total_seconds()) + "c")

    t7 = datetime.datetime.now()
    MergeSort(D)
    t8 = datetime.datetime.now()
    print(C)
    y4.append((t8 - t7).total_seconds())
    print("Слиянием   " + str(N) + "   заняла   " + str((t8 - t7).total_seconds()) + "c")
    print("\n\n")

    table.add_row([str(N), str((t2 - t1).total_seconds()), str((t4 - t3).total_seconds()),
                   str((t6 - t5).total_seconds()), str((t8 - t7).total_seconds())])
print(table)

plt.plot(x, y1, "C0")
plt.plot(x, y2, "C1")
plt.plot(x, y3, "C2")
plt.plot(x, y4, "C3")
plt.show()
