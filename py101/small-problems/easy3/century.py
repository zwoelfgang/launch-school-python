def century(year):
    string = ''
    if year % 10 == 0:
        string = str(year)[:-2]
    else:
        if year > 10:
            string = str(int(str(year)[:-2]) + 1)
        else:
            string = '1'

    if (int(string) % 100 > 10) and (int(string) % 100 < 20):
        return f'{string}th'
    else:
        match int(string) % 10:
            case 1:
                return f'{string}st'
            case 2:
                return f'{string}nd'
            case 3:
                return f'{string}rd'
            case _:
                return f'{string}th'
        

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True
