def clean_up(string):
    idx = 0
    lst = list(string)
    while idx < (len(lst) - 1):
        if idx > 0 and ((idx + 1) < (len(lst) - 1)):
            if not lst[idx - 1].isalpha():
                if not lst[idx].isalpha():
                    if not lst[idx + 1].isalpha():
                        lst.pop(idx - 1)
                        lst[idx - 1] = ' '
                        lst.pop(idx)
                    else:
                        lst.pop(idx - 1)
                        if not lst[idx - 1].isalpha():
                            lst.pop(idx - 1)
                else:
                    lst[idx - 1] = ' '
        else:
            if not lst[idx].isalpha():
                lst[idx] = ' '
            elif not lst[-1].isalpha():
                lst[-1] = ' '
        idx += 1
    return ''.join(lst)

print(clean_up("---what's my +*& line?") == " what s my line ")
# True