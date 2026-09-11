# Tic Tac Toe
import random
import os
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
INITIAL_MARKER = ' '

print('Welcome to Tic Tac Toe!')
print(f'You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}')

def display_board(board):
    os.system('clear')

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

def get_player_move(board):
    while True:
        player_choice = input('Choose a square (1-9) ')
        if player_choice not in board:
            print('Invalid choice. Please try again.')
        elif board[player_choice] != INITIAL_MARKER:
            print('Square already taken. Please try again.')
        else:
            return player_choice

def get_computer_move(board):
    while True:
        computer_choice = random.choice(list(board.keys()))
        if board[computer_choice] == INITIAL_MARKER:
            return computer_choice

def detect_winner(board):
    winning_lines = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['1', '4', '7'],
        ['2', '5', '8'],
        ['3', '6', '9'],
        ['1', '5', '9'],
        ['3', '5', '7'],
        ]   
            
    for line in winning_lines:
        [square_1, square_2, square_3] = line
        if board[square_1] == HUMAN_MARKER and board[square_2] == HUMAN_MARKER and board[square_3] == HUMAN_MARKER:
            return 'Player'
        elif board[square_1] == COMPUTER_MARKER and board[square_2] == COMPUTER_MARKER and board[square_3] == COMPUTER_MARKER:
            return 'Computer'
        
    return False

def board_full(board):
    return INITIAL_MARKER not in board.values()

while True:
    board = initialize_board()
    display_board(board)

    while True:
        player_choice = get_player_move(board)
        board[player_choice] = HUMAN_MARKER
        if detect_winner(board) or board_full(board):
            display_board(board)
            break

        computer_choice = get_computer_move(board)
        board[computer_choice] = COMPUTER_MARKER
        if detect_winner(board) or board_full(board):
            display_board(board)
            break
        
        display_board(board)

    winner = detect_winner(board)
    if winner == 'Player':
        print("Player wins!")
    elif winner == 'Computer':
        print("Computer wins!")
    else: 
        print("It's a tie!")

    answer = input('Play again? (y or n) ')
    if answer.lower() in ['n', 'no']:
        print("Thanks for playing Tic Tac Toe!")
        break