# Спортсмен решил потренироваться перед марафоном и покататься вокруг города на скорость.
# Длина дороги — 123 километра. Спортсмен стартует с нулевого километра и едет со скоростью v километров в час.
# На какой отметке он остановится через t часов?
# Реализуйте программу, которая спрашивает у пользователя v и t и выводит целое число от 0 до 122 — номер километра,
# на котором остановится Спортсмен. Учтите, что он может прокатиться больше одного круга.

import math

# Константы
TIME: str = "Введите значение времени (ч) t = "
VELOCITY: str = "Введите значение скорости (км/ч) v = "
DISTANCE_MAX: int = 123

INPUT_ERROR: str = "Значение {} является некорректным :("
RESULT: str = "Велосипедист проехал {distance} км, сделал {circles} кругов, остановился на отметке {km_mark} км."


# Проверка преобразования типов
def transform_type(value: str) -> bool:
    try:
        value_f: float = float(value)
        if value_f >= 0:
            check = True
        else:
            check = False
    except ValueError:
        check = False
    return check


# Ввод и проверка пользовательских данных
def input_check_user_data(value_request: str) -> float:
    value: str = input(value_request)
    check = transform_type(value)
    while check == False:
        print(INPUT_ERROR.format(value))
        value = input(value_request)
        check = transform_type(value)
    return float(value)


# Задание значений аргументам
def give_value() -> (float, float):
    velocity: float = input_check_user_data(VELOCITY)
    time: float = input_check_user_data(TIME)
    return velocity, time


# Вычисление значений характеристик пройденного спортсменом пути
def calc_result(velocity: float, time: float) -> (float, int, int, int):
    distance: float = velocity * time
    circles: int = distance // DISTANCE_MAX
    # 1-й вариант расчёта отметки расстояния
    km_mark_1: int = math.floor(distance - circles * DISTANCE_MAX)
    # 2-й вариант расчёта отметки расстояния
    if circles == 0:
        km_mark_2 = math.floor(distance)
    else:
        km_mark_2 = math.floor(distance % DISTANCE_MAX)
    return distance, circles, km_mark_1, km_mark_2


# Вывод результатов расчёта
def output_data(distance: float, circles: int, km_mark_1: int):
    print(RESULT.format(distance=distance, circles=circles, km_mark=km_mark_1))


# Основная программа
if __name__ == '__main__':
    velocity, time = give_value()
    distance, circles, km_mark_1, km_mark_2 = calc_result(velocity, time)
    output_data(distance, circles, km_mark_1)
    print(km_mark_2)
