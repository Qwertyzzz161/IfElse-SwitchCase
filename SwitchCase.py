def task1():
    try:
        mark = int(input("Введите свою оценку : "))
    except ValueError:
        print("Нужно ввести целое число. Повторите ввод")
    match mark:
        case 1:
            print("Ваша оценка соответствует <<Плохо>>")
        case 2:
            print("Ваша оценка соответствует <<Неудовлетворительно>>")
        case 3:
            print("Ваша оценка соответствует <<Удовлетворительно>>")
        case 4:
            print("Ваша оценка соответствует <<Хорошо>>")
        case 5:
            print("Ваша оценка соответствует <<Отлично>>")
        case _:
            print("Ошибка")


def task2():
    try:
        month = int(input("Введите номер месяца : "))
    except ValueError:
        print("Нужно ввести целое число. Повторите ввод")
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            print("В этом месяце 31 день")
        case 2:
            print("В этом месяце 28 дней")
        case 4 | 6| 9 | 11:
            print("В этом месяце 30 дней")
        case _:
            print("Ошибка")

def task3():
    try:
        month = int(input("Введите номер месяца : "))
        day = int(input("Введите номер дня : "))
    except ValueError:
        print("Нужно ввести целое число. Повторите ввод")
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            match day:
                case date if 1 <= date <= 30:
                    print(f"Завтра будет {day+1}.{month}")
                case date if  date == 31:
                    print(f"Завтра будет {1}.{month+1}")
                case _:
                    print("Ошибка")
        case 2:
            match day:
                case date if 1 <= date <= 27:
                    print(f"Завтра будет {day+1}.{month}")
                case date if  date == 28:
                    print(f"Завтра будет {1}.{month+1}")
                case _:
                    print("Ошибка")
        case 4 | 6| 9 | 11:
            match day:
                case date if 1 <= date <= 29:
                    print(f"Завтра будет {day+1}.{month}")
                case date if  date == 30:
                    print(f"Завтра будет {1}.{month+1}")
                case _:
                    print("Ошибка")
        case _:
            print("Ошибка")



def task4():
    try:
        place = str(input("В какую сторону света смотрит робот?(N,S,E,W) : "))
    except ValueError:
        print("Нужно ввести букву. Повторите ввод")
    try:
        command = int(input("Какую команду должен выполнить робот? : "))
    except ValueError:
        print("Нужно ввести целое число. Повторите ввод")
    match place:
        case "N":
            match command:
                case direction if direction == 0:
                    print(f"Робот смотрит на север")
                case direction if direction == 1:
                    print(f"Робот смотрит на запад")
                case direction if direction == -1:
                    print(f"Робот смотрит на восток")
                case _:
                    print("Ошибка")
        case "S":
            match command:
                case direction if direction == 0:
                    print(f"Робот смотрит на юг")
                case direction if direction == 1:
                    print(f"Робот смотрит на восток")
                case direction if direction == -1:
                    print(f"Робот смотрит на запад")
                case _:
                    print("Ошибка")
        case "E":
            match command:
                case direction if direction == 0:
                    print(f"Робот смотрит на восток")
                case direction if direction == 1:
                    print(f"Робот смотрит на север")
                case direction if direction == -1:
                    print(f"Робот смотрит на юг")
                case _:
                    print("Ошибка")
        case "N":
            match command:
                case direction if direction == 0:
                    print(f"Робот смотрит запад")
                case direction if direction == 1:
                    print(f"Робот смотрит на юг")
                case direction if direction == -1:
                    print(f"Робот смотрит на север")
                case _:
                    print("Ошибка")
        case _:
            print("Ошибка")


def task5():
    try:
        digit = int(input("Введите число : "))
    except ValueError:
        print("Нужно ввести целое число. Повторите ввод")
    match digit:
        case n if 100 <= n <= 999:
            hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
            tens = ["", "десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
            ones = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
            teens = ["", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]

            hundred_digit = n // 100
            ten_digit = (n % 100) // 10
            one_digit = n % 10

            match (ten_digit, one_digit):
                case (1, d) if d != 0:
                    print(f"{hundreds[hundred_digit]} {teens[d]}")
                case (d, 0) if d != 0:
                    print(f"{hundreds[hundred_digit]} {tens[d]}")
                case (d1, d2):
                    print(f"{hundreds[hundred_digit]} {tens[d1]} {ones[d2]}")
        case _:
            print("Число не находится в диапазоне 100-999")


def task6():
    example = input("Введите выражение в формате <<X + Y>>: ")
    elements = example.split()
    match elements:
        case [num1, '+', num2]:
            result =  int(num1) + int(num2)
        case [num1, '-', num2]:
            result = int(num1) - int(num2)
        case [num1, '*', num2]:
            result = int(num1) * int(num2)
        case [num1, '/', num2] if int(num2) != 0:
            result = int(num1) / int(num2)
        case _:
            return "Ошибка: неверный формат ввода."
    print("Результат =",result)

#task1()
#task2()
#task3()
#task4()
#task5()
#task6()