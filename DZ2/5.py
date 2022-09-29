# Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.

import random
 
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
 
print ('Исходный список :', lst)
mix_lst = random.sample(lst, len(lst))  # shuffle нельзя, ну ладно, возьмем sample, он в отличии от shuffle сохраняет исходный список.
print ('Перемешанный список :', mix_lst)