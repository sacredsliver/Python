# Создайте программу для игры в ""Крестики-нолики"".
import os
os.system('cls')

pole = list(range(1, 10))

win_komb = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
            (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

def draw_pole(): # функция отрисовки игрового поля
    print('-------------')
    for i in range(3):
        print('|', pole[0 + i*3], '|',
              pole[1 + i*3], '|', pole[2 + i*3], '|')
    print('-------------')

def take_hod(player): # фукнция хода игрока
    while True:
        hod = input('Куда поставить ' + player + ' ? ')
        if  hod not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print('Введите вереый номер клеточки для хода')
            continue
        hod = int(hod)
        if str(pole[hod-1]) in 'XO':
            print('Клетка занята, выберите другую')
            continue
        pole[hod-1] = player
        break

def check_win(): # функция проверка на выигрыш
    for elem in win_komb:
        if pole[elem[0]] == pole[elem[1]] == pole[elem[2]]:
            return pole[elem[0]]
    else:
        return False

def game(): # функция самой игры и смены ходов
    a = 0
    while True:
        os.system('cls')
        draw_pole()
        if a % 2 == 0: 
            take_hod('X')
        else:
            take_hod('O')
        if a > 3:
            win = check_win()
            if win:
                os.system('cls')
                draw_pole()
                print(win, 'Выиграл!!!')
                break
        a += 1
        if a > 8:
            os.system('cls')
            draw_pole()
            print('Ничья!!')
            break
game()