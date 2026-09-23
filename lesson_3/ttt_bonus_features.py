import random
import os

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
MATCH_WIN = 5
PLAYER_OPTIONS = ['player', 'computer', 'random']

WINNING_LINES = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],
    [1, 4, 7], [2, 5, 8], [3, 6, 9],
    [1, 5, 9], [3, 5, 7]
]

def prompt(message):
    print(f"=> {message}")

def display_board(board):
    os.system('clear')

    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")
    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print('')

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def join_or(sequence, delimiter=', ', word='or'):
    if len(sequence) == 0:
        return ''
    if len(sequence) == 1:
        return str(sequence[0])
    if len(sequence) == 2:
        return f'{sequence[0]} {word} {sequence[1]}'

    leading_items = delimiter.join(str(item) for item in sequence[:-1])
    
    return f'{leading_items}{delimiter}{word} {sequence[-1]}'

def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square ({join_or(valid_choices)}):")
        square = input().strip()
        if square in valid_choices:
            break

        prompt("Sorry, that's not a valid choice.")

    board[int(square)] = HUMAN_MARKER

def find_at_risk_square(line, board, marker):
    markers_in_line = [board[square] for square in line]

    if markers_in_line.count(marker) == 2:
        for square in line:
            if board[square] == INITIAL_MARKER:
                return square
    return None

def computer_chooses_square(board):
    square = None

    for line in WINNING_LINES:
        square = find_at_risk_square(line, board, COMPUTER_MARKER)
        if square:
            break

    if not square:
        for line in WINNING_LINES:
            square = find_at_risk_square(line, board, HUMAN_MARKER)
            if square:
                break

    if not square and board[5] == INITIAL_MARKER:
        square = 5

    if not square:
        square = random.choice(empty_squares(board))

    board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def detect_winner(board):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
               and board[sq2] == HUMAN_MARKER
               and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER
                  and board[sq2] == COMPUTER_MARKER
                  and board[sq3] == COMPUTER_MARKER):
            return 'Computer'

    return None

def update_score(winner, player_score, computer_score):
    if winner == 'Player':
        player_score += 1
    elif winner == 'Computer':
        computer_score += 1

    return player_score, computer_score

def get_starting_player():
    while True:
        prompt(f'Select a player: {join_or(PLAYER_OPTIONS)}')
        starting_player = input().strip().lower()
        if starting_player not in PLAYER_OPTIONS:
            print(f'Please enter one of the following: {join_or(PLAYER_OPTIONS)}')
        else:
            break

    if starting_player == 'random':
        starting_player = random.choice(['player', 'computer'])
        prompt(f"Random choice: {starting_player} goes first.")
        
    return starting_player

def choose_square(board, current_player):
    if current_player == 'player':
        player_chooses_square(board)
    elif current_player == 'computer':
        computer_chooses_square(board)


def alternate_player(current_player):
    if current_player == 'player':
        return 'computer'
    else:
        return 'player'

def play_one_game(starting_player, scores):
    board = initialize_board()
    current_player = starting_player

    while True:
        display_board(board)
        prompt(f"Score => Player: {scores['Player']}, Computer: {scores['Computer']}")

        choose_square(board, current_player)
        current_player = alternate_player(current_player)

        if someone_won(board) or board_full(board):
            break

    display_board(board)
    return detect_winner(board)

def play_tic_tac_toe():
    while True: 
        scores = {'Player': 0, 'Computer': 0}
        starting_player = get_starting_player()
        
        while scores['Player'] < MATCH_WIN and scores['Computer'] < MATCH_WIN:
            winner = play_one_game(starting_player, scores)   

            if winner:
                scores[winner] += 1
                prompt(f"{winner} won this game!")
            else:
               prompt("It's a tie!")

            if scores['Player'] < MATCH_WIN and scores['Computer'] < MATCH_WIN:
                input("=> Press Enter to start the next round...")
               
        if scores['Player'] == MATCH_WIN:
            prompt("Player won the match!")
        elif scores['Computer'] == MATCH_WIN:
            prompt("Computer won the match!")

        while True:
            prompt("Play again? (y or n)")
            answer = input().strip().lower()

            if answer not in ['y', 'n']:
                print('Please enter y or n')
            else:
                break
        
        if answer == 'n':
            break

    prompt(f"Final Score => Player: {scores['Player']}, Computer: {scores['Computer']}")
    prompt('Thanks for playing Tic Tac Toe!')

play_tic_tac_toe()