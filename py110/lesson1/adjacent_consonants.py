def adjacent_consonants(lst):
    consonants = ['b', 'c', 'd', 'f', 'g', 'h',
                  'j', 'k', 'l', 'm', 'n', 'p',
                  'q', 'r', 's', 't', 'v', 'w',
                  'x', 'y', 'z']
    sorted_lst = []
    counts = []
    count = 0

    for index, item in enumerate(lst):
        stripped_string = item.strip().replace(" ", "").casefold()
        for idx, char in enumerate(stripped_string):
            if idx < len(stripped_string) - 1:
                if char in consonants and stripped_string[idx + 1] in consonants:
                    count += 1
            else:
                if stripped_string[idx - 1] in consonants and char in consonants:
                    count += 1
        counts.insert(index, (lst[index], count))
        count = 0

    counts.sort(key=lambda tup: tup[1], reverse=True)

    for (word, _) in counts:
        sorted_lst.append(word)
    
    return sorted_lst

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(adjacent_consonants(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(adjacent_consonants(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(adjacent_consonants(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(adjacent_consonants(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(adjacent_consonants(my_list))
# ['xxxx', 'xxxb', 'xxxa']
                