board = list(range(1,10))


def show_board(board):
    print("------------")
    for i in range(3):
        print('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
        print("------------")


def take_input(pl_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + pl_token + "? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = pl_token
                valid = True
            else:
                print("Эта клетка уже занята")
        else:
            print("Некорректный ввод, введите число от 1 до 9")


def check_win(board):
    win_cord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in win_cord:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        show_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "Выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья")
            break


main(board)
