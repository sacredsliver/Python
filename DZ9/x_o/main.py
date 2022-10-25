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


# красиво реализованное поле
empty_field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def print_field(field):
    print("┌───┬───┬───┐")
    print("│ "+" │ ".join(field[0])+" │")
    print("├───┼───┼───┤")
    print("│ "+" │ ".join(field[1])+" │")
    print("├───┼───┼───┤")
    print("│ "+" │ ".join(field[2])+" │")
    print("└───┴───┴───┘")


def make_move(field, move, symbol):
    result = field.copy()
    move = move.split()
    [x, y] = list(map(int, move))
    if (3 > x >= 0) and (3 > y >= 0) and result[y][x] == " ":
        result[y][x] = symbol
    else:
        new_attempt = input("Неправильный ход, повторите ввод: ")
        result = make_move(field, new_attempt, symbol)
    return result


def check_win(field):
    # проверка ряда
    for row in field:
        if row[0] == "X" and row[1] == "X" and row[2] == "X":
            return "X"
        if row[0] == "0" and row[1] == "0" and row[2] == "0":
            return "0"
    # проверка колонки
    for col in range(3):
        if field[0][col] == "X" and field[1][col] == "X" and field[2][col] == "X":
            return "X"
        if field[0][col] == "0" and field[1][col] == "0" and field[2][col] == "0":
            return "0"
    # проверка диагонали
    if field[0][0] == "X" and field[1][1] == "X" and field[2][2] == "X":
        return "X"
    if field[0][2] == "X" and field[1][1] == "X" and field[2][0] == "X":
        return "X"
    if field[0][0] == "0" and field[1][1] == "0" and field[2][0] == "0":
        return "0"
    if field[0][2] == "0" and field[1][1] == "0" and field[2][0] == "0":
        return "0"
    return None


field = empty_field
moves_count = 0
is_X_move = True
print("Добро пожаловать в игру X-0. В свой ход вводите координаты, разделенные пробелом.")
while check_win(field) == None and moves_count < 9:
    current_player = "X" if is_X_move else "0"
    field = make_move(field, input(
        f"Ход игрока {current_player}: "), current_player)
    print_field(field)
    is_X_move = not is_X_move
    moves_count += 1
print("Игра окончена")
result = check_win(field)
if result == None:
    print("Ничья")
else:
    print(f"Победитель: игрок {result}")

# Вариант Николая
def field(moves):
    y0 = f"    X1    X2   X3  "
    y1 = f"Y1  {moves['y1']['x1']}  |  {moves['y1']['x2']}  | {moves['y1']['x3']}  "
    y1_1 = "  -----+-----+-----"
    y2 = f"Y2  {moves['y2']['x1']}  |  {moves['y2']['x2']}  | {moves['y2']['x3']}  "
    y1_1 = "  -----+-----+-----"
    y3 = f"Y3  {moves['y3']['x1']}  |  {moves['y3']['x2']}  | {moves['y3']['x3']}  "
    print(y0)
    print(y1)
    print(y1_1)
    print(y2)
    print(y1_1)
    print(y3)

def check(move, moves):
    if len(move) == 4:
        if move[0].lower() == 'y' and move[2].lower() == 'x':
            if move[1] in '123' and move[-1] in '123':
                if moves[move[:2]][move[-2:]] == ' ':
                    return True
                else:
                    print('Данная клетка уже занята.')
            else:
                print('Введены недопустимые значения координат.')
        else:
            print('Вы ввели не допустимые оси координат')
    else:
        print('Введено недопустимое количество символов.')
    print('Попробуйте ещё раз!')
    return False

def wins(moves):
    if ((moves['y1']['x1'] == moves['y1']['x2'] == moves['y1']['x3']
            or moves['y1']['x1'] == moves['y2']['x1'] == moves['y3']['x1']
            or moves['y1']['x1'] == moves['y2']['x2'] == moves['y3']['x3'])
            and moves['y1']['x1'] != ' '):
        return moves['y1']['x1']
    elif ((moves['y2']['x1'] == moves['y2']['x2'] == moves['y2']['x3']
           or moves['y1']['x2'] == moves['y2']['x2'] == moves['y3']['x2']
           or moves['y1']['x3'] == moves['y2']['x2'] == moves['y3']['x1'])
          and moves['y2']['x2'] != ' '):
        return moves['y2']['x2']
    elif ((moves['y3']['x1'] == moves['y3']['x2'] == moves['y3']['x3']
           or moves['y1']['x3'] == moves['y2']['x3'] == moves['y3']['x3'])
          and moves['y3']['x3'] != ' '):
        return moves['y3']['x3']
    return False


def move(symbol, moves, player):
    print('Текущий ход y{}x{}'.format(player[1], player[-1]))
    if player[1] == '1':
        if player[-1] == '1':
            moves['y1']['x1'] = symbol
        elif player[-1] == '2':
            moves['y1']['x2'] = symbol
        else:
            moves['y1']['x3'] = symbol
    elif player[1] == '2':
        if player[-1] == '1':
            moves['y2']['x1'] = symbol
        elif player[-1] == '2':
            moves['y2']['x2'] = symbol
        else:
            moves['y2']['x3'] = symbol
    else:
        if player[-1] == '1':
            moves['y3']['x1'] = symbol
        elif player[-1] == '2':
            moves['y3']['x2'] = symbol
        else:
            moves['y3']['x3'] = symbol
    return moves


moves_out = {
    'y1': {'x1': ' ', 'x2': ' ', 'x3': ' '},
    'y2': {'x1': ' ', 'x2': ' ', 'x3': ' '},
    'y3': {'x1': ' ', 'x2': ' ', 'x3': ' '}
}

field(moves_out)

number_players = int(input('Введите количество игроков (1/2): '))
count_move = 0

if number_players == 2:
    win = False
    while not win and count_move < 9:
        count_move += 1
        player_out = input('Введите координаты хода(пример - y2x3): ')
        while not check(player_out, moves_out):
            player_out = input('Введите координаты хода(пример - y2x3): ')
        if count_move % 2:
            symbol_out = 'X'
        else:
            symbol_out = 'O'
        moves_out = move(symbol_out, moves_out, player_out)

        field(moves_out)
        win = wins(moves_out)
    if count_move == 9:
        print('Ничья!')
    else:
        print(f'На {count_move} ходу победили "{win}"')