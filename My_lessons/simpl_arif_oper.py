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


def arithmetic(text: str)->str:
    symbol=('+-*/.')
    digit=string.digits
    symbol_all=symbol+digit
    znak=''
    point_float = False
    for i in text:
        if i==',':
            return 'Запятая в числе, поставь точку!'
        elif i not in symbol_all:
            return 'Неизвестная операция'
        elif i in symbol and i!='.':
            znak=znak+i
        elif i=='.':
            point_float = True
    if len(znak)!=1:
        return 'Неизвестная операция'
    text_list =text.split(znak[0])
    a=text_list[0]
    b=text_list[1]
    if b=='0':
        return 'ZeroDivisionError'
    if point_float==True:
        d=znak_analiz(znak[0], a, b, point_integer=float)
        return f'{d:.3}'
    else:
        d=znak_analiz(znak[0], a, b)
        return f'{d}'


if __name__=="__main__":
    print(arithmetic('22.44461/0'))

