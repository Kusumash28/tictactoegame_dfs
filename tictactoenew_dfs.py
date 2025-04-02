#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import queue
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True
def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "
def dfs_ai_move(board, player):
    stack = []  # Stack for DFS
    stack.append(board)  # Push the initial board onto the stack

    while stack:
        current_board = stack.pop()  # Pop the top board from the stack

        for row in range(3):
            for col in range(3):
                if current_board[row][col] == " ":  # Check for an empty cell
                    new_board = [row[:] for row in current_board]  # Create a copy of the board
                    new_board[row][col] = player  # Place the player's move
                    if is_winner(new_board, player):  # Check if this move wins the game
                        return row, col  # Return the winning move
                    stack.append(new_board)  # Push the new board onto the stack

    return None  # If no winning move is found, return None
def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    print_board(board)

    while True:
        x_move = input("enterrow and colum(0-2),space separated):").split()
        # Check if the input has two elements before accessing them
        if len(x_move) == 2:  
            try:
                x_row, x_col = int(x_move[0]), int(x_move[1])
                if board[x_row][x_col] != '':
                    print("invalid move try again")
                board[x_row][x_col] = 'X'
                print_board(board)
                if is_winner(board, 'X'):
                    print("Player X(YOU) WINS")
                    break
                if is_draw(board):
                    print("Its a draw")
                    break
            except (ValueError, IndexError):
                print("Invalid input. Please enter two numbers (0-2) separated by a space.")
        else:
            print("Invalid input. Please enter two numbers (0-2) separated by a space.")
                
        print("Player O(computer) turn")
        o_move = dfs_ai_move(board,'O')
        if o_move:
            board[o_move[0]][o_move[1]] = 'O'
            print(f"AI(Computer) moves at {o_move[0]}, {o_move[1]}")
            print_board(board)

            if is_winner(board, 'O'):
                print("player O(COMPUTER) wins")
                break
        else:
            print("Its a draw")
            break

                # main Function
if __name__ == "__main__":
    play_tic_tac_toe()

