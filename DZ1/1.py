# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

import os
os.system('cls')

day = int(input('Введите номер дня недели = '))
if (0<day<6):
    print(day, 'нет', sep=' -> ')
elif (0>=day or day>7):
    print('Такого дня недели не существует')
else: 
    print(day, 'да', sep=' -> ')