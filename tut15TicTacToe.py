from IPython.display import clear_output


def display_board(board):
    # clear_output()
    # print('\n' * 100)
    print(board[7] + "|" + board[8] + "|" + board[9])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[1] + "|" + board[2] + "|" + board[3])


# test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)

def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = (input("Enter O or X for Player 1 : "))
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1, player2)


# print(player_input())

def place_marker(board, marker, position):
    board[position] = marker


# test_board = ['#', 'O', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']

# place_marker(test_board, '$', 8)
# display_board(test_board)


def win_check(board, mark):
    if ([board[7], board[8], board[9]] == [mark, mark, mark] or
            [board[4], board[5], board[6]] == [mark, mark, mark] or
            [board[1], board[2], board[3]] == [mark, mark, mark] or
            [board[1], board[4], board[7]] == [mark, mark, mark] or
            [board[2], board[5], board[8]] == [mark, mark, mark] or
            [board[3], board[6], board[9]] == [mark, mark, mark] or
            [board[7], board[5], board[3]] == [mark, mark, mark] or
            [board[1], board[5], board[9]] == [mark, mark, mark]):
        return True
    else:
        return False


# test_board = ['#', 'O', 'O', 'X', 'O', 'X', 'O', '$', 'O', 'X']

# print(win_check(test_board,'X'))

import random


def choose_first():
    if (random.randint(1, 2)) == 1:
        return "Player1"
    else:
        return "Player2"


# print(choose_first())


def space_check(board, position):
    return board[position] == " "


# test_board = ['#', 'O', 'O', 'X', 'O', ' ', 'O', '$', 'O', 'X']

# print(space_check(test_board,5))

def full_board_check(board):
    return ' ' not in board


# test_board = ['#', 'O', 'O', 'X', 'O', 'X', 'O', '$', 'O', 'X']
# print(full_board_check(test_board))

def player_choice(board,player):
    flag = True
    while flag:
        choice = int(input("Enter the {} choice : ".format(player)))
        if space_check(board, choice):
            return choice

#test_board = ['#', 'O', 'O', ' ', 'O', 'X', 'O', '$', 'O', 'X']
#print(player_choice(test_board))

def replay():
    play_again = " "
    while play_again[0].upper() not in ('Y','N'):
        play_again = input("Do you want to play again ?: ")
    if play_again.upper() == 'Y':
        return True
    else:
        return False


#print(replay())

######################################


print('Welcome to Tic Tac Toe!')

while True:
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    display_board(board)
    player1,player2=player_input()
    print("player1 : " + player1)
    print("player2 : " + player2)

    player1_turn = False
    player2_turn = False

    if choose_first() == "Player1":
        print("Player1 goes first")
        player1_turn = True
    else:
        print("Player2 goes first")
        player2_turn = True

    game_on = True

    while game_on:
        if player1_turn:
            if not full_board_check(board):
                pos1 = player_choice(board,player1)
                place_marker(board, player1, pos1)
                display_board(board)
                if win_check(board, player1):
                    print(f"player 1 {player1} is the winner")
                    game_on = Falses
                    break
                else:
                    player2_turn = True
                    player1_turn = False
            else:
                print("****** GAME DRAW*********")
                break

        else:
            if not full_board_check(board):
                pos2 = player_choice(board,player2)
                place_marker(board, player2, pos2)
                display_board(board)
                if win_check(board, player2):
                    print(f"player 2 {player2} is the winner")
                    game_on = False
                    break
                else:
                    player1_turn = True
                    player2_turn = False
            else:
                print("****** GAME DRAW*********")
                break


    if not replay():
        break
