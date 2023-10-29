# Напишите программу, запрашивающую у пользователя три целых числа и выводящую их в упорядоченном виде – по возрастанию.
# Используйте функции min и max для нахождения наименьшего и наибольшего значений.
# Оставшееся число можно найти путем вычитания из суммы трех введенных чисел максимального и минимального.


# Константы
NUMBERS: str = "Введите три целых числа через пробел: "

INPUT_ERROR: str = "Значение {} не является целым числом :("
RESULT: str = "Упорядоченная последовательность чисел в порядке возрастания: {sort}"


# Проверка преобразования типов
def transform_type(value: str) -> bool:
    try:
        value_int: int = int(value)
        check = True
    except ValueError:
        check = False
    return check


# Ввод и проверка пользовательских данных
def input_check_user_data(value_request: str) -> [int] * 3:
    num_list_str: [str] * 3 = input(value_request).split()
    num_list_int: [int] * 3 = [int] * 3
    for i in range(len(num_list_str)):
        check = transform_type(num_list_str[i])
        while check == False:
            print(INPUT_ERROR.format(num_list_str[i]))
            num_list_str = input(value_request).split()
            for i in range(len(num_list_str)):
                check = transform_type(num_list_str[i])
                if check == False:
                    break
        num_list_int[i] = int(num_list_str[i])
    return num_list_int


# Задание значений аргументам
def give_value() -> ([int] * 3):
    number_list: [int] * 3 = input_check_user_data(NUMBERS)
    return number_list


# Сортировка чисел в порядке возрастания
def sort_list(number_list: [int] * 3) -> ([int] * 3):
    middle: int = sum(number_list) - (max(number_list) + min(number_list))
    return [min(number_list), middle, max(number_list)]


# Вывод результатов расчёта
def output_data(sorted_list: [int] * 3):
    print(RESULT.format(sort=sorted_list))


# Основная программа
if __name__ == '__main__':
    number_list: [int] * 3 = give_value()
    output_data(sorted_list=sort_list(number_list))
