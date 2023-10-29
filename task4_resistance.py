# Дана электрическая цепь, состоящая из 2-х последовательно соединенных проводников (сопротивление каждого известно).
# Найти общее сопротивление цепи (округление результата необходимо выполнить до 1-го знака после запятой).


# Константы
R_1: str = "Введите сопротивление первого проводника (Ом) R1 = "
R_2: str = "Введите сопротивление второго проводника (Ом) R2 = "
INPUT_ERROR: str = "Значение {} является некорректным :("
RESULT: str = "Общее сопротивление цепи: R = {result}"


# Проверка преобразования типов
def transform_type(resistance: str) -> bool:
    try:
        resistance_f: float = float(resistance)
        check = True
    except ValueError:
        check = False
    return check


# Ввод и проверка пользовательских данных
def input_check_user_data(resist_request: str) -> float:
    resistance: str = input(resist_request)
    check = transform_type(resistance)
    while check == False or float(resistance) < 0:
        print(INPUT_ERROR.format(resistance))
        resistance = input(resist_request)
        check = transform_type(resistance)
    return float(resistance)


# Задание значений аргументам
def give_value() -> (float, float):
    r_1: float = input_check_user_data(R_1)
    r_2: float = input_check_user_data(R_2)
    return r_1, r_2


# Вычисление значения общего сопротивления
def calc_resistance(r_1: float, r_2: float):
    return round((r_1 + r_2), 1)


# Вывод результатов расчёта
def output_data(result):
    print(RESULT.format(result=result))


# Основная программа
if __name__ == '__main__':
    resist_1, resist_2 = give_value()
    output_data(calc_resistance(resist_1, resist_2))
