def find_greatest(lst):
    idx = 0
    value = lst[0]
    while idx < len(lst):
        if lst[idx] > value:
            value = lst[idx]
        idx += 1
    return value

collection = [5, 25, 43, -2, 0, 97, 62, 1, -23]

print(find_greatest(collection))
