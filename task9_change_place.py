# Напишите программу, которая меняла бы значения двух переменных местами,
# но без использования третьей переменной и синтаксического сахара,
# а именно — без конструкции a, b = b, a.


# Константы
NUMBER_A: str = "Введите первое целое число A = "
NUMBER_B: str = "Введите второе целое число B = "

INPUT_ERROR: str = "Значение {} не является целым числом :("
ORIGIN: str = "Исходное значение A = {a}\nИсходное значение B = {b}"
RESULT: str = "Нвоое значение A = {a}\nНовое значение B = {b}"


# Проверка преобразования типов
def transform_type(value: str) -> bool:
    try:
        value_int: int = int(value)
        check = True
    except ValueError:
        check = False
    return check


# Ввод и проверка пользовательских данных
def input_check_user_data(value_request: str) -> int:
    value: str = input(value_request)
    check: bool = transform_type(value)
    while check == False:
        print(INPUT_ERROR.format(value))
        value = input(value_request)
        check = transform_type(value)
    return int(value)


# Сортировка чисел в порядке возрастания
def change_value(var_a: int, var_b: int):
    var_a = var_a + var_b
    var_b = var_a - var_b # =var_a
    var_a = var_a - var_b # =var_b
    return var_a, var_b


# Вывод результатов расчёта
def output_data(const: str, a: int, b: int):
    print(const.format(a=a, b=b))


# Основная программа
if __name__ == '__main__':
    var_a: int = input_check_user_data(NUMBER_A)
    var_b: int = input_check_user_data(NUMBER_B)
    output_data(ORIGIN, var_a, var_b)

    var_a, var_b = change_value(var_a, var_b)
    output_data(RESULT, var_a, var_b)
