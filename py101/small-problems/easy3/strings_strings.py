def stringy(num):
    string = ''
    for i in range(num):
        if i % 2 == 0:
            string += '1'
        else:
            string += '0'
    return string

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True
