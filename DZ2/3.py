# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.


is_OK = False
while not is_OK:
    try:
        n = input('Введите число N: ')
        n = float(n)
        n = int(n)
        is_OK = True
    except ValueError:
        print('Вводить надо число')
lst = []
for i in range(1,n+1):
    s = (1+1/i)**i
    s = round(s)
    lst.append(s)
print(f'Полученная сумма последовательности {lst} =', sum(lst))