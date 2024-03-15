my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

evens = []

for list in my_list:
    evens.append([ num for num in list if num % 2 == 0 ])

for list in evens:
    for num in list:
        print(num)
