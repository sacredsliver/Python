# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
# степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
import itertools

k = int(input('Задайте натуральную степень k: '))

lst = list([randint(0, 100) for i in range(k+1)])
print(lst)

def get_poly(k, lst): 
    str1 = ['*x**']*(k-1) + ['*x']
    poly = [[a, b, c] for a, b, c  in itertools.zip_longest(lst, str1, range(k, 1, -1), fillvalue = '')]
    # с помощью этого метода мы объединяем несколько списков в список кортежей с самой длинной итерацией
    # пустые кортежи заполняем пустотой ('')
    print(poly)
    for x in poly:
        x.append(' + ')
    poly = list(itertools.chain(*poly)) # объединяем в один список
    print(poly)
    poly[-1] = ' = 0' # добавляем концовочку (меняем последний '+' на '= 0')
    print(poly)
    return "".join(map(str, poly)).replace(' 1*x',' x') # возвращаем строку без разделителей

s = get_poly(k, lst)
print(s)

with open('Pol1.txt', 'w') as data:
    data.write(s)