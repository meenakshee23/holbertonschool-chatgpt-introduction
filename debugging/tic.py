#!/usr/bin/python3

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Check for draw
        if all(cell != " " for row in board for cell in row):
            print("It's a draw!")
            break

        # Get valid input
        while True:
            try:
                row = int(input(f"Enter row (0-2) for player {player}: "))
                col = int(input(f"Enter column (0-2) for player {player}: "))
                if row in range(3) and col in range(3):
                    if board[row][col] == " ":
                        break
                    else:
                        print("That spot is already taken!")
                else:
                    print("Row and column must be 0, 1, or 2.")
            except ValueError:
                print("Invalid input. Enter an integer 0, 1, or 2.")

        # Make move
        board[row][col] = player

        # Check winner
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Switch player
        player = "O" if player == "X" else "X"

tic_tac_toe()
