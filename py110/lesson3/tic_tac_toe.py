import os

INITIAL_MARKER = ' '
X_MARKER = 'X'
O_MARKER = 'O'
GAMES = 5
WINNING_LINES = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],
    [1, 4, 7], [2, 5, 8], [3, 6, 9],
    [1, 5, 9], [3, 5, 7]
]

def prompt(message):
    print(r'// ' + message + r' \\')

def display_board(board, player_score, computer_score, player_marker, computer_marker):
    os.system('clear')

    prompt(f'You have won {player_score} games. Computer has won {computer_score} games.')
    prompt(f'You are {player_marker}. Computer is {computer_marker}.')
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

def choose_starting_player():
    os.system('clear')

    while True:
        prompt('Welcome to Tic Tac Toe! Would you like to go first? (Y)es or (n)o.')
        answer = input('> ').lower()
        if answer[0] == 'y' or answer[0] == 'n':
            break

        prompt('That choice is invalid, try again.')        
    
    if answer[0] == 'y':
        player_marker = X_MARKER
        computer_marker = O_MARKER
        current_player = 'Player'
    else:
        player_marker = O_MARKER
        computer_marker = X_MARKER
        current_player = 'Computer'
    
    return current_player, player_marker, computer_marker

def choose_player(board, current_player, player_marker, computer_marker):
    if (detect_winner(board, player_marker, computer_marker) == 'Computer'
        or (board_full(board) and current_player == 'Computer')):
        return 'Player', X_MARKER, O_MARKER
    elif (detect_winner(board, player_marker, computer_marker) == 'Player'
          or (board_full(board) and current_player == 'Player')):
        return 'Computer', O_MARKER, X_MARKER
    else:
        return current_player, player_marker, computer_marker

def choose_square(board, current_player, player_marker, computer_marker):
    if current_player == 'Player':
        player_chooses_square(board, player_marker)
        return 'Computer'
    else:
        computer_chooses_square(board, current_player, player_marker, computer_marker)
        return 'Player'
    
def choose_next_square(board, square, current_player, player_marker, computer_marker):
    if current_player == 'Computer':
        board[square] = computer_marker
        current_player = 'Player'
    elif current_player == 'Player':
        board[square] = player_marker
        current_player = 'Computer'

    return current_player

def join_or(lst, delimiter=', ', end='or'):
    match len(lst):
        case 0:
            return ''
        case 1:
            return lst[0]
        case 2:
            return f'{lst[0]} {end} {lst[1]}'
    joined = delimiter.join(num for num in lst[0:-1])
    return f'{joined} {end} {lst[-1]}'

def player_chooses_square(board, player_marker):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square ({join_or(valid_choices)}):")
        square = int(input('> ').strip())
        if square in empty_squares(board):
            break

        prompt('That choice is invalid, try again.')

    board[square] = player_marker

def computer_chooses_square(board, current_player, player_marker, computer_marker):
    if 5 in empty_squares(board):
        square = 5
    else:
        square = best_move(board, current_player, player_marker, computer_marker)

    board[square] = computer_marker

def minimax(board, scores, square, depth, current_player, player_marker, computer_marker):
    if detect_winner(board, player_marker, computer_marker) == 'Computer':
        scores[square].append(10 - depth) 
        return scores
    if detect_winner(board, player_marker, computer_marker) == 'Player':
        scores[square].append(-10 + depth)
        return scores
    if board_full(board):
        scores[square].append(0)
        return scores
    
    if current_player == 'Computer':
        score = float('-inf')
        for sq in board.keys():
            if sq in empty_squares(board):
                current_player = choose_next_square(board, sq, current_player, player_marker, computer_marker)
                score = max(score, *minimax(board, scores, square, depth + 1, current_player, player_marker, computer_marker)[square])
                board[sq] = INITIAL_MARKER
                scores[square].append(score)
    else:
        score = float('inf')
        for sq in board.keys():
            if sq in empty_squares(board):
                current_player = choose_next_square(board, sq, current_player, player_marker, computer_marker)
                score = min(score, *minimax(board, scores, square, depth + 1, current_player, player_marker, computer_marker)[square])
                board[sq] = INITIAL_MARKER
                scores[square].append(score)
    return scores
    
def best_move(board, current_player, player_marker, computer_marker):
    scores = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    best_score = float('-inf')
    for square in empty_squares(board):
        current_player = choose_next_square(board, square, current_player, player_marker, computer_marker)
        scores = minimax(board, scores, square, 0, current_player, player_marker, computer_marker)
        board[square] = INITIAL_MARKER

    for square, score in scores.items():
        if score != []:
            if sum(score) > best_score:
                move = square
                best_score = sum(score)            
    return move

def detect_winner(board, player_marker, computer_marker):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (board[sq1] == player_marker
               and board[sq2] == player_marker
               and board[sq3] == player_marker):
            return 'Player'
        elif (board[sq1] == computer_marker
                  and board[sq2] == computer_marker
                  and board[sq3] == computer_marker):
            return 'Computer'

    return None

def increment_score(board, player_score, computer_score, player_marker, computer_marker):
    if detect_winner(board, player_marker, computer_marker) == 'Player':
        player_score += 1
    elif detect_winner(board, player_marker, computer_marker) == 'Computer':
        computer_score += 1

    return player_score, computer_score

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board, player_marker, computer_marker):
    return bool(detect_winner(board, player_marker, computer_marker))

def display_winner(board, player_marker, computer_marker):
    if someone_won(board, player_marker, computer_marker):
        prompt(f'{detect_winner(board, player_marker, computer_marker)} won!')
    else:
        prompt("It's a tie!")

def play_again(player_score, computer_score):
    if player_score < GAMES and computer_score < GAMES:
        prompt("Play again? (Y)es or (n)o:")
        answer = input('> ').lower()
    else:
        answer = 'n'

    return answer

def display_match_winner(player_score, computer_score):
    if player_score == GAMES:
        prompt(f'Player won the {GAMES} game match!')
    elif computer_score == GAMES:
        prompt(f'Computer won the {GAMES} game match!')

def play_tic_tac_toe():
    player_score = 0
    computer_score = 0
    current_player, player_marker, computer_marker = choose_starting_player()
    board = initialize_board()

    while player_score < GAMES and computer_score < GAMES:
        current_player, \
        player_marker, \
        computer_marker = choose_player(board, current_player, player_marker, computer_marker)
        board = initialize_board()

        while True:
            display_board(board, player_score, computer_score, player_marker, computer_marker)
            current_player = choose_square(board, current_player, player_marker, computer_marker)

            if someone_won(board, player_marker, computer_marker) or board_full(board):
                player_score, \
                computer_score = increment_score(board, player_score, computer_score, player_marker, computer_marker)
                break

        display_board(board, player_score, computer_score, player_marker, computer_marker)
        display_winner(board, player_marker, computer_marker)
        answer = play_again(player_score, computer_score)

        if answer[0] != 'y':
            break

    display_board(board, player_score, computer_score, player_marker, computer_marker)
    display_match_winner(player_score, computer_score)
    prompt('Thanks for playing Tic Tac Toe!')

play_tic_tac_toe()
