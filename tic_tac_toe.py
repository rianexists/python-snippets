from random import randrange
import math

board = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
format = """+-------+-------+-------+
|       |       |       |
|   %s   |   %s   |   %s   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   %s   |   %s   |   %s   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   %s   |   %s   |   %s   |
|       |       |       |
+-------+-------+-------+"""

def display_board(board):
    print(format % (board[0][0],board[0][1],board[0][2],board[1][0],board[1][1],board[1][2],board[2][0],board[2][1],board[2][2]))
    # Ideal process, I'm stupid tho
    #print(format % board[a][a] for a in range(0,3))

def enter_move(board):
    choice = int(input("Where would you like to play (1-9): "))
    while (choice < 1 or choice > 9):
        choice = input("Input out of range, please try again (1-9): ")
    while type(board[math.ceil(int(choice) / 3) - 1][0 if int(choice) % 3 == 1 else 1 if int(choice) % 3 == 2 else 2]) is not int:
        choice = input("This square has already been claimed, please try again: ")
    board[math.ceil(int(choice) / 3) - 1][0 if int(choice) % 3 == 1 else 1 if int(choice) % 3 == 2 else 2] = 'O'
    display_board(board)
    if victory_for(board, 'O'):
        print("You won!")
    else:
        draw_move(board)

def make_list_of_free_fields(board):
    free_spaces = []
    for i in range(0,3):
        for x in range(0,3):
            if type(board[i][x]) is int:
                free_spaces.append((i,x))
    return free_spaces

def victory_for(board, sign):
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        return True
    elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        return True
    elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        return True
    elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        return True
    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        return True
    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        return True
    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    return False

def draw_move(board, choice=randrange(1,10)):
    while type(board[math.ceil(int(choice) / 3) - 1][0 if int(choice) % 3 == 1 else 1 if int(choice) % 3 == 2 else 2]) is not int:
        choice = randrange(1,10)
    board[math.ceil(int(choice) / 3) - 1][0 if int(choice) % 3 == 1 else 1 if int(choice) % 3 == 2 else 2] = 'X'
    display_board(board)
    if victory_for(board, 'X'):
        print("You lost!")
    else:
        enter_move(board)
        
draw_move(board, 5)