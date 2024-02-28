def password(a, b):
    if a == b:
        print("Пароль принят")
    else:
        print("Пароль не принят")

a = input("Введите пароль: ")
b = input("Подтвердите пароль: ")

password(a, b)

def determine_seat_type(seat_number):
    coupe_upper = [1, 2, 3, 4]
    coupe_lower = [5, 6, 7, 8]
    side_upper = [9, 10]
    side_lower = [11, 12]

    if seat_number in coupe_upper:
        return "Верхнее место в купе"
    elif seat_number in coupe_lower:
        return "Нижнее место в купе"
    elif seat_number in side_upper:
        return "Верхнее боковое место"
    elif seat_number in side_lower:
        return "Нижнее боковое место"
    else:
        return "Неверный номер места"

seat_number = int(input("Введите номер места в плацкартном вагоне: "))
print(determine_seat_type(seat_number))


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"Год {year} - високосный")
    else:
        print("Это год не високосный")

year = int(input("Введите год: "))
is_leap_year(year)

def mix_colors(color1, color2):
    if (color1 == "красный" and color2 == "синий") or (color1 == "синий" and color2 == "красный"):
        return "Фиолетовый"
    elif (color1 == "красный" and color2 == "желтый") or (color1 == "желтый" and color2 == "красный"):
        return "Оранжевый"
    elif (color1 == "синий" and color2 == "желтый") or (color1 == "желтый" and color2 == "синий"):
        return "Зеленый"
    else:
        return "Ошибка: введите только 'красный', 'синий' или 'желтый'"

color1 = input("Введите первый цвет: ").lower()
color2 = input("Введите второй цвет: ").lower()
print(mix_colors(color1, color2))
