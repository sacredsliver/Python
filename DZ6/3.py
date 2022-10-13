# Напишите программу, удаляющую из текста все слова, содержащие "абв".

# Было   
import re
text_my = 'Напишите программуабв, удаляющуюабв из текста все словаабв, содержащие "абв"'
old_list = text_my.split()
new_list = [x for x in old_list if not re.search('абв', x)]
my = " ".join(new_list)
print(my)


# Стало
text_my = 'Напишите программуабв, удаляющуюабв из текста все словаабв, содержащие "абв"'
text_my = list(filter(lambda x: 'абв' not in x, text_my.split()))
my = " ".join(text_my)
print(text_my)
print(my)