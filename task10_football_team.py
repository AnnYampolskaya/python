# Составьте программу, которая запрашивает название футбольной команды и повторяет его на экране со словами
# ... - чемпион!
# После этого выполните:
# ●	используя операцию дублирования, нарисуйте черту (набор "-"), длиной, равной размеру названия команды;
# ●	преобразуйте строку в нижний регистр и выведите на экран:
#   ○	длину наименования команды;
#   ○	есть ли в наименовании команды буква "п" (True/False)?
#   ○	сколько раз повторяется буква "а"?


# Константы
TEAM: str = "Введите название футбольной команды: "
LINE: str = "-"

CHAMPION: str = "{team} - чемпион! "
LEN_TEAM_NAME: str = "Длина наименования команды {team} равна {len_team} символов."
FIND_SYMBOL: str = "Название команды {team} {include}содержит букву '{symbol}'."
AMOUNT_SYMBOL: str = "В названии команды {team} буква '{symbol}' встречается {amount} раз."

SYMB_P: str = "п"
SYMB_A: str = "а"


# Поиск буквы в названии команды
def find_symbol(team_name: str, symbol: str) -> str:
    including: str = ""
    if not symbol in team_name:
        including = "не "
    return including


# Подсчёт количества заданной буквы в названии команды
def compute_symbol(team_name: str, symbol: str) -> int:
    symb_amount: int = 0
    for char in team_name:
        if char == symbol:
            symb_amount += 1
    return symb_amount


# Основная программа
if __name__ == '__main__':
    team_name: str = input(TEAM).strip()
    print(CHAMPION.format(team=team_name))

    len_team = len(team_name)
    print(LINE * len_team)

    team_name_low: str = team_name.lower()
    print(LEN_TEAM_NAME.format(team=team_name_low, len_team=len_team))
    print(FIND_SYMBOL.format(team=team_name_low, include=find_symbol(team_name_low, SYMB_P), symbol=SYMB_P))
    print(AMOUNT_SYMBOL.format(team=team_name_low, symbol=SYMB_A, amount=compute_symbol(team_name_low, SYMB_A)))
