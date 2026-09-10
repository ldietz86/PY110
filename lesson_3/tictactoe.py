# Tic Tac Toe
import random
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
INITIAL_MARKER = ' '

print('Welcome to Tic Tac Toe!')

def display_board(board):
    print(f'You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}')

    print('')
    print('     |     |')
    print(f"  {board['1']}  |  {board['2']}  |  {board['3']}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board['4']}  |  {board['5']}  |  {board['6']}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board['7']}  |  {board['8']}  |  {board['9']}")
    print('     |     |')
    print('')

def initialize_board():
    board = {}
        
    for square in range(1, 10):
        board[str(square)] = INITIAL_MARKER
        
    return board

board = initialize_board()
display_board(board)