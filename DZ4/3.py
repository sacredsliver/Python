# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

# Первый вариант, через множество
numbers = [1, 2, 2, 3, 3, 4, 4, 5, 5]
unikum_numbers = list(set(numbers))
print(unikum_numbers)


# Второй вариант, с сохранением того же порядка 
import numpy
numbers = [1, 2, 2, 3, 3, 4, 4, 5, 5]
res = numpy.array(numbers)
unikum_numbers = numpy.unique(res)
print(unikum_numbers)