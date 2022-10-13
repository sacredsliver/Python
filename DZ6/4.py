# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.


is_OK = True
while is_OK:
    try:
        n = input('Введите число N: ')
        n = float(n)
        n = int(n)
        is_OK = False
    except ValueError:
        print('Вводить надо число')
lst = []

# было
for i in range(1,n+1):
    s = (1+1/i)**i
    s = round(s)
    lst.append(s)
print(f'Полученная сумма последовательности {lst} =', sum(lst))

# стало
lst = [round((1+1/i)**i) for i in range(1,n+1)]
print(f'Полученная сумма последовательности {lst} =', sum(lst))