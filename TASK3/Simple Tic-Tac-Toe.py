# Simple Tic-Tac-Toe (User vs Computer)
# Internship Project - Main Flow Services and Technologies

import random

board = [" " for _ in range(9)]

def print_board():
    print("\n")
    for i in range(3):
        print(board[3*i], "|", board[3*i+1], "|", board[3*i+2])
        if i < 2:
            print("--+---+--")

def check_winner(symbol):
    win_conditions = [(0,1,2), (3,4,5), (6,7,8),
                      (0,3,6), (1,4,7), (2,5,8),
                      (0,4,8), (2,4,6)]
    for a,b,c in win_conditions:
        if board[a] == board[b] == board[c] == symbol:
            return True
    return False

def player_move():
    move = int(input("Enter your move (1-9): ")) - 1
    if board[move] == " ":
        board[move] = "X"
    else:
        print("Spot already taken!")
        player_move()

def computer_move():
    available = [i for i in range(9) if board[i] == " "]
    move = random.choice(available)
    board[move] = "O"

# Main Game
print("TIC-TAC-TOE GAME (Simple Version)")
print_board()

for _ in range(9):
    player_move()
    print_board()
    if check_winner("X"):
        print("You Win!")
        break

    if " " not in board:
        print("It's a Draw!")
        break

    computer_move()
    print_board()
    if check_winner("O"):
        print("Computer Wins!")
        break
