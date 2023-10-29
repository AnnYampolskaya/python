# Константы
X: str = "Введите целое число x = "
Y: str = "Введите целое число y = "
Z: str = "Введите целое число z = "
INPUT_ERROR: str = "{} не является целым числом :("
RESULT: str = "Результат выполнения операции: F = {result}"


# Ввод и проверка пользовательских данных
def input_check_user_data(arg_request: str) -> int:
    argument: str = input(arg_request)
    while argument.isdecimal() == False:
        print(INPUT_ERROR.format(argument))
        argument = input(arg_request)
    return int(argument)


# Задание значений аргументам
def give_value() -> (int, int, int):
    x: int = input_check_user_data(X)
    y: int = input_check_user_data(Y)
    z: int = input_check_user_data(Z)
    return x, y, z


# Вычисление значения  функции
def calc_function(x: int, y: int, z: int):
    func = (((x ** 5 + 7) / (abs(-6) * y)) ** (1 / 3)) / (7 - z % y)
    return round(func, 3)


# Вывод результатов расчёта
def output_data(result):
    print(RESULT.format(result=result))


# Основная программа
if __name__ == '__main__':
    x, y, z = give_value()
    result = calc_function(x, y, z)
    output_data(result=result)
