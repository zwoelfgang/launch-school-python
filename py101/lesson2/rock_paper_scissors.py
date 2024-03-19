import random
import os
import platform

VALID_CHOICES = {
    ('(r)ock', 'r', 'rock'): 'rock',
    ('(p)aper', 'p', 'paper'): 'paper',
    ('(sc)issors', 'sc', 'scissors'): 'scissors',
    ('(sp)ock', 'sp', 'spock'): 'spock',
    ('(l)izard', 'l', 'lizard'): 'lizard'
}

WINNING_MOVES = {
    'rock': ('scissors', 'lizard'),
    'paper': ('rock', 'spock'),
    'scissors': ('paper', 'lizard'),
    'spock': ('rock', 'scissors'),
    'lizard': ('paper', 'spock')
}

TOTAL_GAMES = 5

def prompt(message):
    print(r'\\', message, r'//')

def unpack_valid_choices():
    return [item for item_list in list(VALID_CHOICES) for item in item_list]

def unpack_displayable_choices(choices):
    return [item for item in choices
            if choices.index(item) % len(list(VALID_CHOICES)[0]) == 0]

def unpack():
    choices = unpack_valid_choices()
    displayable_choices = unpack_displayable_choices(choices)

    return choices, displayable_choices

def get_player_choice(choices_list):
    prompt(f"Choose one: {', '.join(choices_list)}.")
    choice = input('>> ').lower()

    return choice

def map_player_choice(string):
    idx = 0
    choice_map = {}
    choice_key = None

    while idx < len(list(VALID_CHOICES)):
        tup = list(VALID_CHOICES)[idx]
        for item in tup:
            if item == string:
                choice_map[tup] = VALID_CHOICES[tup]
                choice_key = tup
        idx += 1

    return choice_map, choice_key

def check_player_choice(choice, display_list, total_list):
    choice_map, key = map_player_choice(choice)

    while choice not in total_list:
        prompt(f"That choice is invalid. \
Please enter {', '.join(display_list)}")
        choice = input('>> ').lower()
        choice_map, key = map_player_choice(choice)

    return choice_map, key

def get_computer_choice():
    return random.choice(list(VALID_CHOICES.values()))

def display_choices(player, computer):
    prompt(f'You chose {player}, computer chose {computer}.')

def play_again(player_score):
    if player_score == 5:
        prompt('Congratulations! You won best out of 5. \
Would you like to play again? (Y)es or (n)o.')
    else:
        prompt('Oh no, you were defeated by the computer in best out of 5. \
Would you like to play again? (Y)es or (n)o.')

    string = input('>> ').lower()
    string = check_answer(string)

    return string

def check_answer(string):
    while string == '' or (string[0] != 'y' and string[0] != 'n'):
        prompt('That choice is invalid. Please enter (y)es or (n)o.')
        string = input('>> ').lower()

    return string

def determine_winner(player, computer):
    if computer in WINNING_MOVES[player]:
        return 'player'
    elif player in WINNING_MOVES[computer]:
        return 'computer'
    else:
        return None

def display_winner(won, player, computer):
    if won in ['player', 'computer']:
        prompt(f'You picked {player}, \
the computer picked {computer}: {won} won!')
    else:
        prompt(f"You picked {player}, \
the computer picked {computer}: it's a tie!")

def increment_score(won, player, computer):
    if won == 'player':
        return player + 1, computer
    if won == 'computer':
        return player, computer + 1

    return player, computer

def display_score(player, computer):
    prompt(f"Your score is {player}. The computer's score is {computer}.")

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def game_loop(player_score, computer_score, num_games):
    while player_score < TOTAL_GAMES and computer_score < TOTAL_GAMES:
        clear_screen()

        if num_games > 0:
            display_winner(winner, map_choice[key_choice], choice_comp)

        display_score(player_score, computer_score)
        choices, displayable_choices = unpack()
        choice = get_player_choice(displayable_choices)
        map_choice, key_choice = check_player_choice(choice,
                                                     displayable_choices,
                                                     choices)
        choice_comp = get_computer_choice()
        display_choices(map_choice[key_choice], choice_comp)
        winner = determine_winner(map_choice[key_choice], choice_comp)
        player_score, computer_score = increment_score(winner,
                                                       player_score,
                                                       computer_score)

        num_games += 1
    
    return winner, \
           map_choice[key_choice], \
           choice_comp, \
           player_score, \
           computer_score

def play_game():
    while True:
        player_score = 0
        computer_score = 0
        num_games = 0

        winner, \
        player, \
        computer, \
        player_score, \
        computer_score = game_loop(player_score, computer_score, num_games)

        clear_screen()
        display_winner(winner, player, computer)
        display_score(player_score, computer_score)
        answer = play_again(player_score)

        if answer[0] == 'y':
            player_score = 0
            computer_score = 0
        elif answer[0] == 'n':
            clear_screen()
            break

play_game()
