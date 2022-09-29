# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

is_OK = False
while not is_OK:
    try:
        n = input('Введите число больше 1: ')
        n = float(n)
        n = int(n)
        if n > 1:
            is_OK = True
    except ValueError:
        print('Вводить надо числа больше 1!')
lst = [1]
for i in range(2, n+1):
    lst.append(lst[i-2] * i)
print('Получился список =', lst)