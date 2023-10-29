# Дано двузначное и трехзначное число.
# Для каждого выведите на экран сумму и произведение цифр.


import math

# Константы
DOUBLE: str = "Введите двузначное число A = "
TRIPLE: str = "Введите трёхзначное число B = "

INPUT_ERROR: str = "Значение {} является некорректным :("
RESULT: str = "Сумма цифр числа {number} равна {sum}. Произведение цифр числа {number} равно {production}"


# Проверка преобразования типов
def transform_type(value: str) -> bool:
    try:
        value_int: int = int(value)
        if value_int >= 0:
            check = True
        else:
            check = False
    except ValueError:
        check = False
    return check


# Ввод и проверка пользовательских данных
def input_check_user_data(value_request: str) -> int:
    value: str = input(value_request)
    check = transform_type(value)
    while check == False:
        print(INPUT_ERROR.format(value))
        value = input(value_request)
        check = transform_type(value)
    return int(value)


# Задание значений аргументам
def give_value() -> (int, int):
    double: int = input_check_user_data(DOUBLE)
    triple: int = input_check_user_data(TRIPLE)
    return double, triple


# Вычисление значений суммы и произведения цифр числа
def calc_result(number: int) -> (int, int, int, int):
    digit_list: [int] = [int(digit) for digit in str(number)]
    sum_1 = 0
    prod_1 = 1
    for digit in digit_list:
        sum_1 += digit
        prod_1 *= digit
    sum_2: int = sum(digit_list)
    prod_2: int = math.prod(digit_list)
    return sum_1, sum_2, prod_1, prod_2


# Вывод результатов расчёта
def output_data(number: int, sum: int, production: int):
    print(RESULT.format(number=number, sum=sum, production=production))


# Основная программа
if __name__ == '__main__':
    double_number, triple_number = give_value()
    double_sum_1, double_sum_2, double_prod_1, double_prod_2 = calc_result(double_number)
    triple_sum_1, triple_sum_2, triple_prod_1, triple_prod_2 = calc_result(triple_number)

    output_data(double_number, double_sum_1, double_prod_1)
    output_data(double_number, double_sum_2, double_prod_2)
    output_data(triple_number, triple_sum_1, triple_prod_1)
    output_data(triple_number, triple_sum_2, triple_prod_2)
