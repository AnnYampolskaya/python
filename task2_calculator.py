# Составьте программу, которая запрашивает у пользователя 2 целых числа и выполняет операции:
# арифметические: +, -, * , / , // , %, **, log10;
# сравнение: <, <=, >, >=, !=, ==,
# выводя на экран результат каждого действия.
# В случае получение вещественного результата,
# округлите его до 2-х знаков после запятой (используя функцию round()).
# Подсказка. Функцию log10 вы найдете в модуле math.


import math

# Константы
NUMBER_1: str = "Введите первое целое число: "
NUMBER_2: str = "Введите второе целое число: "
INPUT_ERROR: str = "{} не является целым числом :("
OPERATION: str = "Из списка {} выберите операцию, которую требуется произвести над числами. Введите знак операции: "
RESULT: str = "Результат выполнения операции: {num_1} {operation} {num_2} = {result}"

OPER_F1: dict = {'+': '(прибавить)',
                 '-': '(вычесть)',
                 '*': '(умножить)',
                 '/': '(поделить)',
                 '//': '(поделить без остатка)',
                 '%': '(найти остаток от деления)',
                 '**': '(возвести в степень)',
                 'log10': '(найти логарифм числа по основанию 10)',
                 '<': '(строго меньше)',
                 '<=': '(меньше или равно)',
                 '>': '(строго больше)',
                 '>=': '(больше или равно)',
                 '!=': '(не равно)',
                 '==': '(равно)',
                 }


# Ввод и проверка пользовательских данных
def input_check_user_data(number_request: str):
    user_num: str = input(number_request)
    while user_num.isdecimal() == False:
        print(INPUT_ERROR.format(user_num))
        user_num = input(number_request)
    return int(user_num)


# Задание значений операндов
def give_value() -> (int, int, str):
    user_num_1: int = input_check_user_data(NUMBER_1)
    user_num_2: int = input_check_user_data(NUMBER_2)
    user_oper: str = input(OPERATION.format(OPER_F1))
    return user_num_1, user_num_2, user_oper


# Расчёт результата операции
def calc_operation(num_1: int, num_2: int, operation: str):
    operation_dict: dict = {'+': int('{x}'.format(x=num_1)) + int('{y}'.format(y=num_2)),
                            '-': int('{x}'.format(x=num_1)) - int('{y}'.format(y=num_2)),
                            '*': int('{x}'.format(x=num_1)) * int('{y}'.format(y=num_2)),
                            '/': int('{x}'.format(x=num_1)) / int('{y}'.format(y=num_2)),
                            '//': int('{x}'.format(x=num_1)) // int('{y}'.format(y=num_2)),
                            '%': int('{x}'.format(x=num_1)) % int('{y}'.format(y=num_2)),
                            '**': int('{x}'.format(x=num_1)) ** int('{y}'.format(y=num_2)),
                            'log10': math.log(int('{x}'.format(x=num_1)), int('{y}'.format(y=num_2))),
                            '<': int('{x}'.format(x=num_1)) < int('{y}'.format(y=num_2)),
                            '<=': int('{x}'.format(x=num_1)) <= int('{y}'.format(y=num_2)),
                            '>': int('{x}'.format(x=num_1)) > int('{y}'.format(y=num_2)),
                            '>=': int('{x}'.format(x=num_1)) >= int('{y}'.format(y=num_2)),
                            '!=': int('{x}'.format(x=num_1)) != int('{y}'.format(y=num_2)),
                            '==': int('{x}'.format(x=num_1)) == int('{y}'.format(y=num_2)),
                            }

    result = operation_dict[operation]
    # округление вещественных чисел до 2ух знаков после запятой
    if type(result) == float:
        result = round(result, 2)
    return result


# Вывод результатов расчёта
def output_data(num_1: int, num_2: int, operation: str, result):
    print(RESULT.format(num_1=num_1, operation=operation, num_2=num_2, result=result))


# Основная программа
if __name__ == '__main__':
    user_num_1, user_num_2, user_oper = give_value()
    result = calc_operation(user_num_1, user_num_2, user_oper)
    output_data(num_1=user_num_1, num_2=user_num_2, operation=user_oper, result=result)
