# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import os
from random import randint
os.system('cls')

konfety = 2021  # Указать сколько конфет на кону

def type_game(): # функция выбора типа игры, два человека или с ботом
    is_OK = True
    while is_OK:
        try:
            select = int(input('Выберете вариант игры (2 - игра в двоем, любое другое число - игра с ботом) - '))
            if select == 2:
                user1 = input('Игорок 1, представьтесь - ')
                user2 = input('Игорок 2, представьтесь - ')
                gamer = user1
                is_OK = False
            else:
                user1 = input('Игорок 1, представьтесь - ')
                user2 = 'bot'
                gamer = user1
                is_OK = False
        except ValueError:
            print()
    return user1, user2, gamer

def take_hod(player): # фукнция хода игрока 
    global konfety
    while True:
        try:
            hod = int(input('Сколько взять конфет (1-28),  ' + player + ' ? '))
            if hod >= 1 and hod <= 28 and hod <= konfety:
                konfety -= hod
                os.system('cls')
                break
            else:
                print('Введите от 1 до 28 для хода')
                continue
        except ValueError:
            print()
        break

def check_win(): # функция проверка на выигрыш
    if konfety == 0:
        return True
    else:
        return False

def bot(): # функция хода бота
    global konfety
    while True:
        hod = randint(1, 28)
        if konfety <= 28:
            hod = konfety
            konfety -= hod
            print('Бот взял', hod, 'конфет')
            break
        if hod <= konfety:
            konfety -= hod
            print('Бот взял', hod, 'конфет')
            break
        else:
            continue

def game(): # функция самой игры и смены ходов
    a = 0 # счетчик ходов
    b = 2 # константа для проверки выиграша
    user1, user2, gamer = type_game()
    while True:
        print('Осталось', konfety, 'конфет')
        if a % 2 == 0: # если ход четный, ходит первый игрок
            take_hod(user1)
            gamer = user1
        elif user2 in 'bot':
            bot()
            gamer = 'Бот'
        else:
            take_hod(user2)
            gamer = user2
        if b > konfety // 28: # проверка выигрыша начинаеться только если осталось чуть более двух ходов
            win = check_win()
            if win:
                os.system('cls')
                print(gamer, 'Выиграл!!!')
                break
        a += 1 # счетчик ходов
        print(konfety//28)

game()