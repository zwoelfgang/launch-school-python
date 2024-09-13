def clean_up(string):
    idx = 0
    lst = list(string)
    for index in range(len(lst)):
        if not lst[index].isalpha():
            lst.pop(index)
            lst.insert(index, ' ')
    while idx < len(lst):
        if lst[idx] == ' ' and (idx < len(lst) - 1):
            if lst[idx + 1] == ' ':
                lst.pop(idx + 1)
                if lst[idx - 1] == ' ':
                    lst.pop(idx - 1)
                elif lst[idx + 1] == ' ':
                    lst.pop(idx + 1)
            elif lst[idx - 1] == ' ':
                lst.pop(idx - 1)
        idx += 1
    return ''.join(lst)

print(clean_up("---what's my +*& line?"))# == " what s my line ")
print(clean_up('9U N9n 9uu9 nU( ub(   ((((Ppo P p))000)))'))
# True