# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input('Введите число: '))
print(k)
nego = [1,-1]
fibo = [1,1]
for i in range(2,k):
    list = fibo[i-1]+fibo[i-2]
    fibo.append(list)
for x, elem in enumerate(fibo, 2):
    if x % 2 != 0:
        lst_nego = elem * -1
        nego.append(lst_nego)
    else:
        nego.append(elem)
nego.reverse()
nego.append(0)
print(nego+fibo)