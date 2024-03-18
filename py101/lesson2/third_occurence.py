def third_occurence(string, char):
    idx = 0
    counter = 0
    while idx < len(string):
        if string[idx] == char:
            counter += 1
        if counter == 3:
            return idx
        idx += 1
    return None
        

print(third_occurence('axbxcdxex', 'x'))
print(third_occurence('Hi budddy how\'s it going?', 'x'))
