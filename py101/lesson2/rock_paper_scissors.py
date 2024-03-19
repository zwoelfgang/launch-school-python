import random
import os

VALID_CHOICES = {
    ('(r)ock', 'r', 'rock'): 'rock',
    ('(p)aper', 'p', 'paper'): 'paper',
    ('(sc)issors', 'sc', 'scissors'): 'scissors',
    ('(sp)ock', 'sp', 'spock'): 'spock',
    ('(l)izard', 'l', 'lizard'): 'lizard'
}

def prompt(message):
    print(r'\\', message, r'//')

def unpack_valid_choices():
    return [item for item_list in list(VALID_CHOICES) for item in item_list]

def unpack_displayable_choices():
    return [item for item in choices_list
            if choices_list.index(item) % len(list(VALID_CHOICES)[0]) == 0]

def get_user_choice(choices):
    prompt(f"Choose one: {', '.join(choices)}.")
    choice = input('>> ').lower()

    return choice

def map_user_choice(string):
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

def check_user_choice(choice, display_list, total_list):
    choice_map, key = map_user_choice(choice)

    while choice not in total_list:
        prompt(f"That choice is invalid. \
Please enter {', '.join(display_list)}")
        choice = input('>> ').lower()
        choice_map, key = map_user_choice(choice)

    return choice_map, key

def get_computer_choice():
    return random.choice(list(VALID_CHOICES.values()))

def display_choices(player, computer):
    prompt(f'You chose {player}, computer chose {computer}.')

def play_again(player_num):
    if player_num == 5:
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
    match (player, computer):
        case ('rock', 'scissors') | \
             ('rock', 'lizard') | \
             ('paper', 'rock') | \
             ('paper', 'spock') | \
             ('scissors', 'paper') | \
             ('scissors', 'lizard') | \
             ('spock', 'rock') | \
             ('spock', 'scissors') | \
             ('lizard', 'paper') | \
             ('lizard', 'spock'):
            return 'player'
        case ('scissors', 'rock') | \
             ('lizard', 'rock') | \
             ('rock', 'paper') | \
             ('spock', 'paper') | \
             ('paper', 'scissors') | \
             ('lizard', 'scissors') | \
             ('rock', 'spock') | \
             ('scissors', 'spock') | \
             ('paper', 'lizard') | \
             ('spock', 'lizard'):
            return 'computer'
        case _:
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

while True:
    player_score = 0
    computer_score = 0
    num_games = 0
    winner = ''
    user_choice_map = {}
    user_key = ()
    computer_choice = ''

    while player_score < 5 and computer_score < 5:
        os.system('clear')

        if num_games > 0:
            display_winner(winner, user_choice_map[user_key], computer_choice)

        display_score(player_score, computer_score)

        choices_list = unpack_valid_choices()
        displayable_choices_list = unpack_displayable_choices()

        user_choice = get_user_choice(displayable_choices_list)
        user_choice_map, user_key = check_user_choice(user_choice,
                                                      displayable_choices_list,
                                                      choices_list)

        computer_choice = get_computer_choice()

        display_choices(user_choice_map[user_key], computer_choice)
        winner = determine_winner(user_choice_map[user_key], computer_choice)

        player_score, computer_score = increment_score(winner,
                                                       player_score,
                                                       computer_score)

        num_games += 1

    os.system('clear')

    display_winner(winner, user_choice_map[user_key], computer_choice)
    display_score(player_score, computer_score)

    answer = play_again(player_score)

    if answer[0] == 'y':
        player_score = 0
        computer_score = 0
    elif answer[0] == 'n':
        os.system('clear')
        break
