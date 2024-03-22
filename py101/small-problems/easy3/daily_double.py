def crunch(string):
    lst = list(string)
    idx = 0
    while idx < len(lst) - 1:
        if lst[idx] == lst[idx + 1]:
            lst.pop(idx)
            idx -= 1
        idx += 1
    return ''.join(lst)
            

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')
