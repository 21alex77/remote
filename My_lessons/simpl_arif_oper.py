import string

# Написать функцию arithmetic, принимающую 3 аргумента:
# первые 2 - числа, третий - операция, которая должна быть произведена над ними.
# Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе).
# В остальных случаях вернуть строку "Неизвестная операция".

'''
Функция для арифметических операций (+, -, *, /)
1) проверка состоит ли строка только из цифр и знаков из symbola, 
   если нет то вернуть строку "Неизвестная операция"
2) проверить сколько знаков операции в входной строке, если не 1 то "Неизвестная операция"
3) проверить вторая цифра ноль, если да то return 'ZeroDivisionError'
4) проверить  цифра является float, если да то переменная point_float принимаем True 
если point_float=True, то значение арифметической операции возвращаем с .00
5) проверить есть ли вначале строки знак -, если есть то znak_minus принимаем True
6) проверка check_zero на неправильно указанное число 0006, "Неизвестная операция"
'''


def znak_analiz(znak, a, b, point_integer=int):
    if znak[0] == '+':
        c = point_integer(a) + point_integer(b)
        return c
    elif znak[0] == '-':
        c = point_integer(a) - point_integer(b)
        return c
    elif znak[0] == '*':
        c = point_integer(a) * point_integer(b)
        return c
    elif znak[0] == '/':
        c = point_integer(a) / point_integer(b)
        return c


def znak_analiz_minus(znak, a, b, point_integer=int):
    if znak[1] == '+':
        c = - point_integer(a) + point_integer(b)
        return c
    elif znak[1] == '-':
        c = - point_integer(a) - point_integer(b)
        return c
    elif znak[1] == '*':
        c = - point_integer(a) * point_integer(b)
        return c
    elif znak[1] == '/':
        c = - point_integer(a) / point_integer(b)
        return c


def check_zero(text_list) -> bool:
    caunt = 0
    for i in text_list:
        if '.' not in i and i[0] == '0':
            caunt += 1
    if caunt > 0:
        return True
    else:
        return False


def arithmetic(text: str) -> str:
    symbol = ('+-*/.')
    digit = string.digits
    symbol_all = symbol + digit
    znak = ''
    point_float = False
    znak_minus = False
    for i in text:
        if i == ',':
            return 'Запятая в числе, поставь точку!'
        elif i not in symbol_all:
            return 'Неизвестная операция'
        elif i in symbol and i != '.':
            znak = znak + i
        elif i == '.':
            point_float = True
    if len(znak) > 2 or len(text) == 0:
        return 'Неизвестная операция'
    elif len(znak) == 2 and text[0] != '-':
        return 'Неизвестная операция'
    elif '-' == text[0]:
        znak_minus = True
    if znak_minus == True:
        if znak[1]=='-':
            text_list = text.split(znak[1])
            text_list.remove('')
        else:
            text_list = text.split(znak[1])
            text_list[0] = text_list[0].replace('-', '')
        a = text_list[0]
        b = text_list[1]
        zero = check_zero(text_list)
        if b == '0':
            return 'ZeroDivisionError'
        elif zero == True:
            return 'Неизвестная операция'
        elif point_float == True:
            e = znak_analiz_minus(znak, a, b, point_integer=float)
            return f'{e:.2f}'
        else:
            e = znak_analiz_minus(znak, a, b)
            if type(e) == float:
                return f'{e:.2f}'
            else:
                return f'{e}'
    else:
        text_list = text.split(znak[0])
        a = text_list[0]
        b = text_list[1]
        zero = check_zero(text_list)
        if b == '0':
            return 'ZeroDivisionError'
        elif zero == True:
            return 'Неизвестная операция'
        elif point_float == True:
            d = znak_analiz(znak, a, b, point_integer=float)
            return f'{d:.2f}'
        else:
            d = znak_analiz(znak, a, b)
            if type(d) == float:
                return f'{d:.2f}'
            else:
                return f'{d}'


if __name__ == "__main__":
    print(arithmetic('-6-0005'))
