# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

lst = [2, 3, 4, 5, 6]
proizved_lst = []

# было
for i in range((len(lst)+1)//2):
    proizved_lst.append(lst[i]*lst[-1-i])
print(proizved_lst)

# стало
proizved_lst = [(lst[i]*lst[-1-i]) for i in range((len(lst)+1)//2)]
print(proizved_lst)