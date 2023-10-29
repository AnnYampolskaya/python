# Составьте программу, которая запрашивает название государства и его столицы, а затем выводит сообщение:
# Государство - ..., столица - ...
# На месте многоточий должны быть выведены соответствующие значения.


# Константы
COUNTRY: str = "Введите название страны: "
CAPITAL: str = "Введите название столицы: "
RESULT: str = "Государство - {country}, столица - {capital}"

# Основная программа
if __name__ == '__main__':
    country: str = input(COUNTRY).strip()
    capital: str = input(CAPITAL).strip()

    print(RESULT.format(country=country.title(), capital=capital.title()))
