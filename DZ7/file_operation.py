from UI import get_data as gd

info = gd()
def writing_csv ():
    file = 'Phonebook.csv'
    print('data', info)
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')

def writing_txt ():
    file = 'Phonebook.txt'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {info[0]}\n\nИмя: {info[1]}\n\nНомер телефона: {info[2]}\n\nОписание: {info[3]}\n\n\n')

def open_csv ():
    with open('Phonebook.csv', 'r', encoding = 'utf-8') as data:
        text_phone = data.read()
    print(text_phone)
    

