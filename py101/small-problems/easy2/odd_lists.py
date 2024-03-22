def oddities(lst):
    new_lst = []
    for idx in range(0, len(lst), 2):
        new_lst.append(lst[idx])
    return new_lst

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True
