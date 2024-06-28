def task1():
    try:
        a = int(input("Введите значение a : "))
        b = int(input("Введите значение b : "))
        c = int(input("Введите значение c : "))
    except ValueError:
        print("Нужно ввести целое число. Повторите ввод")
    if (a == 0 and b == 0 and c == 0):
        print("Три переменных равны нулю")
    elif ((a == 0 and b == 0 and not c == 0)
          or (a == 0 and not b == 0 and c == 0)
          or (not a == 0 and b == 0 and c == 0)):
        print("Две переменных равны нулю")
    elif a == 0 or b == 0 or c == 0:
        print("Одна из переменных равна нулю")
    else:
        print("Ни одна из переменных не равна нулю")


def task2():
    try:
        a = int(input("Введите значение a : "))
        b = int(input("Введите значение b : "))
    except ValueError:
        print("Нужно ввести целое число. Повторите ввод")
    if a > b:
        print(f"Большее число = {a}")
    elif a < b:
        print(f"Большее число = {b}")
    elif a == b:
        print("Числа равны")


def task3():
    try:
        a = int(input("Введите значение a : "))
        b = int(input("Введите значение b : "))
    except ValueError:
        print("Нужно ввести целое число. Повторите ввод")
    if a > b:
        print(f"Большее число = {a}, меньшее число = {b}")
    elif a < b:
        print(f"Большее число = {b}, меньшее число = {a}")
    elif a == b:
        print("Числа равны")

def task4():
    try:
        a = int(input("Введите значение a : "))
        b = int(input("Введите значение b : "))
    except ValueError:
        print("Нужно ввести целое число. Повторите ввод")
    if a > b:
        print(f"Меньшее число = {b}")
    elif a < b:
        print(f"Меньшее число = {a}")
    elif a == b:
        print("Числа равны")


def task5():
    try:
        x = int(input("Введите значение x : "))
        y = int(input("Введите значение y : "))
    except ValueError:
        print("Нужно ввести целое число. Повторите ввод")
    if x > 0 and y > 0:
        print("Точка лежит в 1 четверти")
    elif x < 0 and y > 0:
        print("Точка лежит в 2 четверти")
    elif x < 0 and y < 0:
        print("Точка лежит в 3 четверти")
    elif x > 0 and y < 0:
        print("Точка лежит в 4 четверти")
    elif x == 0 and y == 0:
        print("Точка лежит в центре координатной плоскости")
    else:
        print("Точка лежит на пересечении двух четвертей")

#task1()
#task2()
#task3()
#task4()
#task5()


