dictionary = {
    'one': (1, 'one'),
    'two': (2, 'two'),
    'three': (3, 'three')
}

def change_dictionary():
    for key, value in dictionary.items():
        dictionary[key] = (str(value[0]), value[1])

change_dictionary()
print(dictionary)
