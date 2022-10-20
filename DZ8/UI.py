import model as md
import controller as con
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def input_int(msg=""):
    while True:
        try:
            result = int(input(msg))
        except ValueError:
            print("Ошибка, повторите ввод")
        else:
            return result

def main_menu():
    # cls()
    global finish
    print('Добро пожаловать в БД')
    print('Введите номер операции:')
    print('Показать все записи справочника - 1')
    print('Добавить запись - 2')
    print('Удалить запись - 3')
    print('Выход - 0')
    option = input_int()
    if option == 1:
        db = con.open_db()
        md.print_db(db)
        input("Нажмите Enter для продолжения...")
    elif option == 2:
        db = con.open_db()
        md.add(db)
        input("Нажмите Enter для продолжения...")
    elif option == 3:
        md.print_db(con.open_db())
        md.del_value(input_int("Введите номер записи для удаления: "))
        input("Нажмите Enter для продолжения...")
    elif option == 0:
        finish = True

finish = False
while not finish:
    main_menu()