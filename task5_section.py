# Дано уравнение ax + b = 0 и отрезок [m;n]. Ответьте на вопрос, попадает ли решение уравнения в указанный отрезок.


# Константы
KOEF_A: str = "Введите значение коэффициента (a <> 0) а = "
KOEF_B: str = "Введите значение коэффициента b = "
LIMIT_M: str = "Введите значение левой граничной точки отрезка m = "
LIMIT_N: str = "Введите значение правой граничной точки отрезка n = "

ERROR_SECTION_LIMITS: str = "Некорректные значения концов отрезка"
INPUT_ERROR: str = "Значение {} является некорректным :("
RESULT: str = "Решение x = {x} уравнения {a} * x + {b} = 0 {result} в заданный отрезок [{m}; {n}]."


# Проверка преобразования типов
def transform_type(value: str) -> bool:
    try:
        value_f: float = float(value)
        check = True
    except ValueError:
        check = False
    return check


# Ввод и проверка пользовательских данных
def input_check_user_data(value_request: str) -> float:
    value: str = input(value_request)
    check = transform_type(value)
    if value_request == KOEF_A and value == 0:
        check = False
    while check == False:
        print(INPUT_ERROR.format(value))
        value = input(value_request)
        check = transform_type(value)
    return float(value)


# Задание значений аргументам
def give_value() -> (float, float, float, float):
    a: float = input_check_user_data(KOEF_A)
    b: float = input_check_user_data(KOEF_B)
    m: float = input_check_user_data(LIMIT_M)
    n: float = input_check_user_data(LIMIT_N)
    while (m >= n):
        print(ERROR_SECTION_LIMITS)
        m = input_check_user_data(LIMIT_M)
        n = input_check_user_data(LIMIT_N)
    return a, b, m, n


# Проверка попадания корней уравнения в заданный отрезок
def calc_result(a: float, b: float, m: float, n: float) -> (float, bool):
    x: float = (-b) / a
    return x, m <= x <= n


# Вывод результатов расчёта
def output_data(x: float, a: float, b: float, result: str, m: float, n: float):
    print(RESULT.format(x=x, a=a, b=b, result=result, m=m, n=n))


# Основная программа
if __name__ == '__main__':
    a_koef, b_koef, m_left_limit, n_right_limit = give_value()
    x, in_section = calc_result(a_koef, b_koef, m_left_limit, n_right_limit)

    result: str = ""
    if in_section:
        result = "попадает"
    else: result = "не попадает"
    output_data(x, a_koef, b_koef, result, m_left_limit, n_right_limit)
