def concatenate(lst):
    result = ''
    for string in lst:
        result += string
    return result

string_list = ['Hi', ' how', ' are', ' ya', '?']

print(concatenate(string_list))
