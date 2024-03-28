def password(a, b):
 a = input("Введите пароль: ")
 b = input("Подтвердите пароль: ")
if a == b:
        print("Пароль принят")
    else:
        print("Пароль не принят")

password(a, b)

def determine_seat_type(seat_number):
    if seat_number % 2 == 0 and seat_number <= 18:
        return "Верхнее место в купе"
    elif seat_number % 2 != 0 and seat_number <= 18:
        return "Нижнее место в купе"
    elif seat_number % 2 == 0 and seat_number > 18 and seat_number <= 54:
        return "Верхнее боковое место"
    elif seat_number % 2 != 0 and seat_number > 18 and seat_number <= 54:
        return "Нижнее боковое место"
    else:
        return "Выберете масто в вагоне (54 мест): "

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
