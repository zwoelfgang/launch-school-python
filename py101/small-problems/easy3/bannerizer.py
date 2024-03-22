def print_in_box(string):
    print('+-' + ('-' * len(string)) + '-+')
    print('| ' + (' ' * len(string)) + ' |')
    print('| ' + string + ' |')
    print('| ' + (' ' * len(string)) + ' |')
    print('+-' + ('-' * len(string)) + '-+')

print_in_box('To boldly go where no one has gone before.')
print_in_box('')
