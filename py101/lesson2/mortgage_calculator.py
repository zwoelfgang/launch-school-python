import os
import json

def message(text):
    print(r'\\', text, r'//')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

def is_zero_or_less(number_str):
    if float(number_str) <= 0:
        return True

    return False

def is_less_than_zero(number_str):
    if float(number_str) < 0:
        return True

    return False

def invalid_answer(string):
    if string == '':
        return True
    if string[0].lower() == 'y' or string[0].lower() == 'n':
        return False

    return True

def get_number(string):
    message(MESSAGES[string])
    number = input(MESSAGES['prompt'])

    if string == 'apr':
        while invalid_number(number) or is_less_than_zero(number):
            message(MESSAGES['invalid_number'])
            number = input(MESSAGES['prompt'])
    else:
        while invalid_number(number) or is_zero_or_less(number):
            message(MESSAGES['invalid_number'])
            number = input(MESSAGES['prompt'])

    return number

def get_answer():
    message(MESSAGES['try_again'])
    answer = input(MESSAGES['prompt'])

    while invalid_answer(answer):
        message(MESSAGES['invalid_answer'])
        answer = input(MESSAGES['prompt'])

    return answer

def calculate_monthly_payment(principal_str, apr_str, loan_duration_str):
    amount = float(principal_str)
    monthly_rate = (float(apr_str) / 100) / 12
    months = float(loan_duration_str) * 12

    if monthly_rate:
        payment = amount * \
            (monthly_rate / (1 - (1 + monthly_rate) ** (-months)))
    else:
        payment = amount / months

    payment=round(payment, 2)

    return payment

def display_monthly_payment():
    message(MESSAGES['monthly_payment'].format(payment=monthly_payment))

with open('mortgage_calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

message(MESSAGES['welcome'])

while True:
    os.system('clear')

    principal = get_number('principal')
    apr = get_number('apr')
    loan_duration = get_number('loan_duration')

    monthly_payment = calculate_monthly_payment(principal, apr, loan_duration)

    display_monthly_payment()

    play_again = get_answer()

    if play_again[0].lower() == 'n':
        os.system('clear')
        break
