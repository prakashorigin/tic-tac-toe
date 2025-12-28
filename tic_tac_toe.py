"""
TIC TAC TOE GAME IN PYTHON

WORKFLOW OF PROJECT:
1. Display the game board
2. Player chooses a position (1–9)
3. Computer chooses a position randomly
4. Check win or tie condition
5. Display result

Board positions:
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
"""

import random

# Create empty board
board = [" "] * 9

# Display board function
def display_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

# Check win condition
def check_win(player):
    win_combinations = [
        (0,1,2), (3,4,5), (6,7,8),   # rows
        (0,3,6), (1,4,7), (2,5,8),   # columns
        (0,4,8), (2,4,6)             # diagonals
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Check tie
def check_tie():
    return " " not in board

# Main game loop
print("Welcome to Tic Tac Toe!")
display_board()

while True:
    # Player move
    user_move = int(input("Enter your move (1-9): ")) - 1

    if board[user_move] != " ":
        print("Position already taken! Try again.")
        continue

    board[user_move] = "X"
    display_board()

    if check_win("X"):
        print("🎉 You win!")
        break

    if check_tie():
        print("It's a Tie!")
        break

    # Computer move
    comp_move = random.choice([i for i in range(9) if board[i] == " "])
    board[comp_move] = "O"
    print("Computer played:")
    display_board()

    if check_win("O"):
        print("💻 Computer wins!")
        break

    if check_tie():
        print("It's a Tie!")
        break
