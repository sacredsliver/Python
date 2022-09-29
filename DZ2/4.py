# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число

n = int(input('Введите число N: '))
lst_number = [i for i in range(-n, n+1)]
print('список чисел', lst_number)
file_index = open('file.txt', 'r')
proizv = 1
lst_index = []
for i in file_index:
    index = int(i.strip())
    lst_index.append(lst_number[index])
    proizv *= lst_number[index]
print('Произведение', lst_index, 'равно =', proizv)
file_index.close()