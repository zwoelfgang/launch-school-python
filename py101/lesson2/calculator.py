import json

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

def operate(number_str):
    match number_str:
        case '1':
            output = float(number1) + float(number2)
        case '2':
            output = float(number1) - float(number2)
        case '3':
            output = float(number1) * float(number2)
        case '4':
            output = float(number1) / float(number2)
        case _:
            output = None

    return output

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

print(MESSAGES['welcome'])

while True:
    print(MESSAGES['first_number'])
    number1 = input('>> ')

    while invalid_number(number1):
        print(MESSAGES['invalid_number'])
        number1 = input('>> ')

    print(MESSAGES['second_number'])
    number2 = input('>> ')

    while invalid_number(number2):
        print(MESSAGES['invalid_number'])
        number2 = input('>> ')

    print(MESSAGES['operation_type'])
    operation = input('>> ')

    while not operate(operation):
        print(MESSAGES['invalid_operation'])
        operation = input('>> ')

    print(MESSAGES['result'].format(output=operate(operation)))
    print(MESSAGES['try_again'])
    answer = input('>> ')

    if answer.lower() == 'n' or answer.lower() == 'no':
        break
