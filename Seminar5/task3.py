# Создайте программу для игры в ""Крестики-нолики"".
# Для определения победы вам может пригодиться функция filter.
# Проверяйте победу после каждого хода, фильтруя столбцы, строки и диагонали по знаку хода

board = list(range(1, 10))


def draw_board(board):
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
"""
Задаем поле
"""


def take_input(player_token):
    val = False
    while not val:
        player_answer = input("Куда поставим " + player_token+"? \n")
        try:
            player_answer = int(player_answer)

        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                val = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")
"""
Создаем функцию определяющую какую позицию выбирает игрок для входа
Проверяем введено ли положительное число от 1 - 9
"""


def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


"""
Создаем функцию проверяющую поле, для этого создаем кортеж с выигрышными координатами
"""


def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "ВЫИГРАЛ!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)


"""
с помощью счетчика ходов опредялем победителя
"""

main(board)

input("Нажмите enter для выхода!")
