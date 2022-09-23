# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import os
os.system('cls')


def input_num(x):
    xy = ['X', 'Y']
    a = []
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = int(input(f'Введите координату по {xy[i]}: '))
                a.append(number)
                is_OK = True
            except ValueError:
                print('Вводить надо целые числа!')
    return a


def calc_length(a, b):
    length = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return length

print('Введите координаты точки А')
point_a = input_num(2)
print('Введите координаты точки В')
point_b = input_num(2)
print(f"Длина отрезка: {format(calc_length(point_a, point_b), '.2f')}")


