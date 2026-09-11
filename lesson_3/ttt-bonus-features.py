import random
import os

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
MATCH_WIN = 5

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

def join_or(lst, separator=', ', last_separator='or'):
    if not lst:
        return ""
    if len(lst) == 2:
        return f'{lst[0]} {last_separator} {lst[1]}'
    if len(lst) > 2:
        last_num = str(lst[-1])
        result = ""
        for idx in range(len(lst) - 1):
            result += f'{lst[idx]}{separator}'
        result += f'{last_separator} {last_num}'
        return result
    return str(lst[0])

def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square ({join_or(valid_choices)}):")
        square = input().strip()
        if square in valid_choices:
            break

        prompt("Sorry, that's not a valid choice.")

    board[int(square)] = HUMAN_MARKER

def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return
    square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def detect_winner(board):
    winning_lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]

    for line in winning_lines:
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

def play_tic_tac_toe():
    while True: 
        player_score = 0
        computer_score = 0
        
        while player_score < MATCH_WIN and computer_score < MATCH_WIN:
            board = initialize_board()
            
            while True:
                display_board(board)
                prompt(f"Score => Player: {player_score}, Computer: {computer_score}")

                player_chooses_square(board)
                if someone_won(board) or board_full(board):
                    break

                computer_chooses_square(board)
                if someone_won(board) or board_full(board):
                    break

            display_board(board)

            winner = detect_winner(board)

            player_score, computer_score = update_score(
                winner,
                player_score,
                computer_score
            )

            if winner:
                prompt(f"{winner} won this game!")
            else:
               prompt("It's a tie!")

            if player_score < MATCH_WIN and computer_score < MATCH_WIN:
                input("=> Press Enter to start the next round...")
               
        if player_score == MATCH_WIN:
            prompt("Player won the match!")
        elif computer_score == MATCH_WIN:
            prompt("Computer won the match!")

        prompt("Play again? (y or n)")
        answer = input().lower()

        if answer[0] != 'y':
            break

    prompt(f"Final Score => Player: {player_score}, Computer: {computer_score}")
    prompt('Thanks for playing Tic Tac Toe!')

play_tic_tac_toe()
