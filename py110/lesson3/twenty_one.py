import os
import random
import time

SUITS = ['\u2660', '\u2665', '\u2666', '\u2663']
VALUES = [['2', 2],
          ['3', 3],
          ['4', 4],
          ['5', 5],
          ['6', 6],
          ['7', 7],
          ['8', 8],
          ['9', 9],
          ['10', 10],
          ['J', 10],
          ['Q', 10],
          ['K', 10],
          ['A', 11]]
ROUNDS = 5

def initialize_deck():
    return [[suit, value] for suit in SUITS for value in VALUES]

def shuffle(deck):
    return random.shuffle(deck)

def deal_cards(deck):
    house_hand = []
    player_hand = []

    for _ in range(2):
        house_hand.append(deck.pop(0))
        player_hand.append(deck.pop(0))

    return house_hand, player_hand

def show_cards(house_hand, player_hand, house_wins, player_wins, reveal=False):
    os.system('clear')

    prompt(f'This is a {ROUNDS} round game of blackjack.')
    prompt(f'You have won {player_wins} rounds and the house has won {house_wins} rounds.')
    print('')
    print('House hand:')
    print('+-----+' * len(house_hand))
    if not reveal:
        print('|     |', end='', flush=True)
        for num in range(1, len(house_hand)):
            print(f'|{house_hand[num][0][0]}    |', end='', flush=True)
        print('\r')
        print('|  ?  |', end='', flush=True)
        for num in range(1, len(house_hand)):
            if house_hand[num][1][0] == '10':
                print(f'|  {house_hand[num][1][0]} |', end='', flush=True)
            else:
                print(f'|  {house_hand[num][1][0]}  |', end='', flush=True)
    else:
        for num in range(len(house_hand)):
            print(f'|{house_hand[num][0][0]}    |', end='', flush=True)
        print('\r')
        for num in range(len(house_hand)):
            if house_hand[num][1][0] == '10':
                print(f'|  {house_hand[num][1][0]} |', end='', flush=True)
            else:
                print(f'|  {house_hand[num][1][0]}  |', end='', flush=True)
    print('')
    print('|     |' * len(house_hand))
    print('+-----+' * len(house_hand))
    print('')
    print('Player hand:')
    print('+-----+' * len(player_hand))
    for num in range(len(player_hand)):
        print(f'|{player_hand[num][0][0]}    |', end='', flush=True)
    print('\r')
    for num in range(len(player_hand)):
        if player_hand[num][1][0] == '10':
            print(f'|  {player_hand[num][1][0]} |', end='', flush=True)
        else:
            print(f'|  {player_hand[num][1][0]}  |', end='', flush=True)
    print('')
    print('|     |' * len(player_hand))
    print('+-----+' * len(player_hand))
    print('')

def prompt(message):
    print(r'// ' + message + r' \\')

def count_total(hand):
    values = []
    aces = 0

    for num in range(len(hand)):
        values.append(hand[num][1][1])
        if hand[num][1][0] == 'A':
            aces += 1

    if aces > 1:
        if (sum(values) - ((aces - 1) * 10)) > 21:
            total = sum(values) - (aces * 10)
        else:
            total = sum(values) - ((aces - 1) * 10)
    elif aces == 1 and sum(values) > 21:
        total = sum(values) - 10
    else:
        total = sum(values)

    return total

def player_turn(deck, player_hand):
    prompt('Your turn! Would you like to hit or stay?')

    while True:
        answer = input('> ').lower()
        if answer in ('hit', 'stay'):
            break

        prompt('Sorry, that response is invalid. Hit or stay?')

    if answer == 'hit':
        player_hand.append(deck.pop(0))

    return player_hand, answer

def house_turn(deck, house_hand):
    total = count_total(house_hand)

    if total < 17:
        answer = 'hit'
        house_hand.append(deck.pop(0))
    else:
        answer = 'stay'

    return house_hand, answer

def busted(total):
    return total > 21

def play_twenty_one():
    house_wins = 0
    player_wins = 0
    while house_wins < ROUNDS and player_wins < ROUNDS:
        deck = initialize_deck()
        shuffle(deck)
        house_hand, player_hand = deal_cards(deck)
        while True:
            show_cards(house_hand, player_hand, house_wins, player_wins)
            player_hand, answer = player_turn(deck, player_hand)
            show_cards(house_hand, player_hand, house_wins, player_wins)
            player_total = count_total(player_hand)
            if answer == 'stay' or busted(player_total):
                break

        if busted(player_total):
            house_wins += 1
            prompt('You busted! Play again? (Y)es or (n)o:')
            answer = input('> ').lower()
            if answer[0] == 'n':
                break
            continue
        prompt('You chose to stay.')

        while True:
            show_cards(house_hand, player_hand, house_wins, player_wins)
            house_hand, answer = house_turn(deck, house_hand)
            time.sleep(2)
            show_cards(house_hand, player_hand, house_wins, player_wins)
            house_total = count_total(house_hand)
            if answer == 'stay' or busted(house_total):
                break

        show_cards(house_hand, player_hand, house_wins, player_wins, True)

        if busted(house_total):
            player_wins += 1
            prompt('The house busted! Play again? (Y)es or (n)o:')
            answer = input('> ').lower()
            if answer[0] == 'n':
                break
            continue
        prompt('The house chose to stay.')

        if player_total > house_total:
            player_wins += 1
            prompt('Congratulations, you won! Play again? (Y)es or (n)o:')
            answer = input('> ').lower()
            if answer[0] == 'n':
                break
        else:
            house_wins += 1
            prompt('The house wins! Play again? (Y)es or (n)o:')
            answer = input('> ').lower()
            if answer[0] == 'n':
                break

    show_cards(house_hand, player_hand, house_wins, player_wins, True)
    prompt(f'The {ROUNDS} rounds are up! Thanks for playing!')

play_twenty_one()
