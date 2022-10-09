# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

import os
os.system('cls')

def encode_file(my_text):  # функция кодировая текста
    str_code = ''
    count = 1       
    for i in range(len(my_text)):
        if i < len(my_text)-1:
            if my_text[i] == my_text[i + 1]:
                count += 1
            else:
                str_code += str(count) + my_text[i]
                count = 1
        else:
            str_code += str(count) + my_text[i]
    return str_code

def decode_file(str_code): # функция раскодирования текста
    count = ''
    my_text = ''
    for i in str_code:
        if i.isdigit():
            count += i
        else:
            my_text += i * int(count)
            count = ''
    return my_text


with open('decode.txt', 'r') as data: # считали исходный текст
    my_text = data.read()

print('Исходный текст', my_text)
code_text = encode_file(my_text) # закодировали исходный текст
print('Текст после кодирования', code_text)

with open('encode.txt', 'w') as data: # записали закодированный текст
    data.write(code_text)
    
with open('encode.txt', 'r') as data: # считали закодированый текст
    str_code = data.read()

my_text = decode_file(str_code) # раскодировали текст
print('Раскодированный текст', my_text)


