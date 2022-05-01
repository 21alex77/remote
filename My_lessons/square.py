# Task 3: Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата.


'''
Функция для определения  периметр квадрата, площадь квадрата и диагональ квадрата square:
1) если не число то 'Неизвестная операция'
2) если перед числом -, то 'Уберите минус'
3) периметр квадрата-perimetr_square; площадь квадрата-area_square; диагональ квадрата-diagonal_square
4) вывод кортежа data
'''


def square(argument: str) -> tuple:
    try:
        float(argument)
    except (ValueError, TypeError):
        return 'Неизвестная операция'
    if '-' in argument:
        return 'Уберите минус'
    else:
        a = float(argument)
    perimetr_square = 4 * a
    area_square = a ** 2
    diagonal_square = (2 ** (0.5)) * a
    data = (float(f'{perimetr_square:.3f}'), float(f'{area_square:.3f}'), float(f'{diagonal_square:.3f}'))
    return data


if __name__ == "__main__":
    print(square('4.6'))
