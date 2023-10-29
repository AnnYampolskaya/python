# Напишите программу, запрашивающую у пользователя число
# и подсчитывающую сумму натуральных положительных чисел от 1 до введенного пользователем значения.
# Сумма первых n положительных чисел может быть рассчитана по формуле: sum = (n*(n+1))/2


# Константы
POS_NUMBER: str = "Введите любое положительное число: "
RESULT_SUM: str = "Сумма положительных чисел от 1 до {} равна {}"


# Ввод данных пользователем
def input_user_data() -> int:
    pos_number = int(input(POS_NUMBER))
    return pos_number


# Расчёт суммы натуральных положительных чисел от 1 до введенного пользователем значения
def calc_n_pos_numbers_sum(user_number: int) -> int:
    return (user_number * (user_number + 1)) / 2


# Вывод результатов расчёта
def output_data(user_number: int, sum: int):
    print(RESULT_SUM.format(user_number, sum))


# Основная программа
if __name__ == '__main__':
    user_number: int = input_user_data()
    sum: int = calc_n_pos_numbers_sum(user_number)
    output_data(user_number, sum)