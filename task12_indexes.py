# Дано слово объектно-ориентированный. Используя индексацию и срезы составьте из него слова:
# объект, ориентир, тир, кот, рента и выведите их на экран.

# Константы
WORD: str = "объектно-ориентированный"

RESULT: str = "Государство - {country}, столица - {capital}"

# Основная программа
if __name__ == '__main__':
    object: str = WORD[:6]
    landmark: str = WORD[9:17]
    shoot_gal: str = WORD[14:17]
    cat: str = WORD[4] + WORD[0] + WORD[5]
    renta: str = WORD[10]+WORD[12:15]+WORD[-5]

    print("Исходное слово:", WORD)
    print(object)
    print(landmark)
    print(shoot_gal)
    print(cat)
    print(renta)
