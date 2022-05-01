# Task: Написать функцию long_years, принимающую 1 аргумент — год, и возвращающую 'Високостный год',
#       если год високосный, и 'Обычный год' иначе.

'''
Функция для определения високостного года long_years:
1) високосный год 1 раз в 4 года
2) 2020 был високосным следующий в 2024, т.е. год%4==0
3) проверить если 0 и знак минус, то "Неизвестная операция"
4) если год закачивается на 00, т.е. начало века то не високосный кроме исключений spisok_exceptions(00, 400, 800...)
'''


def long_years(year: str) -> str:
    spisok_exceptions = (i for i in range(0, 1000000, 400))
    try:
        int(year) == int
    except ValueError:
        return 'Неизвестная операция'
    if year == '0' or int(year) < 0:
        return 'нет данных'
    elif int(year) in spisok_exceptions:
        return 'Високостный год'
    elif year[-2:] == '00':
        return 'Обычный год'
    elif int(year) % 4 == 0:
        return 'Високостный год'
    else:
        return 'Обычный год'


if __name__ == "__main__":
    print(long_years('1941'))
