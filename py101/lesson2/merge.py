def merge(lst1, lst2):
    idx = 0
    lst = []
    while idx < len(lst1) or (idx < len(lst2)):
        lst.append(lst1[idx])
        lst.append(lst2[idx])
        idx += 1
    return lst

print(merge([1, 2, 3], [4, 5, 6])) # => [1, 4, 2, 5, 3, 6]
