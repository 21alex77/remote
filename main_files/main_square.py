import My_lessons

if __name__ == "__main__":
    peremen = My_lessons.square(input('Введите число:\n'))
    if type(peremen) != tuple:
        print(peremen)
    else:
        print(f'Периметр квадрата: {peremen[0]}')
        print(f'Площадь квадрата: {peremen[1]}')
        print(f'Диагональ квадрата: {peremen[2]}')
