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

def invalid_answer(string):
    if string == '':
        return True
    if string[0].lower() == 'y' or string[0].lower() == 'n':
        return False

    return True

with open('mortgage_calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

message(MESSAGES['welcome'])

while True:
    message(MESSAGES['principal'])
    principal = input(MESSAGES['prompt'])

    while invalid_number(principal) or is_zero_or_less(principal):
        message(MESSAGES['invalid_number'])
        principal = input(MESSAGES['prompt'])

    message(MESSAGES['apr'])
    apr = input(MESSAGES['prompt'])

    while invalid_number(apr) or is_zero_or_less(apr):
        message(MESSAGES['invalid_number'])
        apr = input(MESSAGES['prompt'])

    message(MESSAGES['loan_duration'])
    loan_duration = input(MESSAGES['prompt'])

    while invalid_number(loan_duration) or is_zero_or_less(loan_duration):
        message(MESSAGES['invalid_number'])
        loan_duration = input(MESSAGES['prompt'])

    principal = float(principal)
    monthly_rate = (float(apr) / 100) / 12
    months = float(loan_duration) * 12
    monthly_payment = principal * \
        (monthly_rate / (1 - (1 + monthly_rate) ** (-months)))

    monthly_payment=round(monthly_payment, 2)

    message(MESSAGES['monthly_payment'].format(payment=monthly_payment))

    message(MESSAGES['try_again'])
    answer = input(MESSAGES['prompt'])

    while invalid_answer(answer):
        message(MESSAGES['invalid_answer'])
        answer = input(MESSAGES['prompt'])

    if answer[0].lower() == 'n':
        break
