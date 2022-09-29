# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23isinstance
# - 0,56 -> 11

is_OK = False
while not is_OK:
    try:
        num = input('Введите вещественное число: ')
        num = num.replace('-', '')
        num = num.replace('.', '')
        n = list(num)
        n = [int(digit) for digit in n]
        is_OK = True
    except ValueError:
        print('Вводить надо вещественное число!')

suma = sum(n)
print('Сумма цифр числа равна =', suma)

# можно еще вот так
# num = float(num)
# num = abs(num)
# summ = sum(map(int, str(num).replace('.', '')))
# print('Сумма цифр числа равна =', summ)