# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# *Пример:* 
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# было
my_list = [1, 2, 3, 5, 1, 5, 3, 10]
new_list = []
for i in range(len(my_list)):
    if my_list.count(my_list[i]) == 1:
        new_list.append(my_list[i])
print(new_list)

# стало
enum_number = list(map(int, input("input list:").split()))
enum_unique = list(filter(lambda item: enum_number.count(item) == 1, enum_number))
print(enum_number, '->', enum_unique)