my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

my_dict = { key: len(key) for key in my_set if len(key) % 2 == 1 }
print(my_dict)
