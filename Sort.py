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


def InsertionSort(A):  # сортировка вставками
    for i in range(len(A) - 1):
        j = i + 1
        while j > 0 and A[j] > A[j - 1]:
            A[j], A[j - 1] = A[j - 1], A[j]
            j -= 1


table = prettytable.PrettyTable(["Размер списка", "Время пузырька", "Время вставки"])
x = []
y1 = []
y2 = []

for N in range(1000, 5001, 1000):
    x.append(N)
    min = 1
    max = N
    A = []
    for i in range(N):
        A.append(int(round(random.random() * (max - min) + min)))

    B = A.copy()

    t1 = datetime.datetime.now()
    BubbleSort(A)
    t2 = datetime.datetime.now()
    y1.append((t2 - t1).total_seconds())
    print("Пузырьковая сортировка   " + str(N) + "   заняла   " + str((t2 - t1).total_seconds()) + "c")

    t3 = datetime.datetime.now()
    InsertionSort(B)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Вставками   " + str(N) + "   заняла   " + str((t4 - t3).total_seconds()) + "c")

    table.add_row([str(N), str((t2 - t1).total_seconds()), str((t4 - t3).total_seconds())])
print(table)

plt.plot(x, y1, "C0")
plt.plot(x, y2, "C1")
plt.show()
