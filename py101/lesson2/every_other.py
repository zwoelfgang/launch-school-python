def every_other(lst):
    idx = 0
    result = []
    while idx < len(lst):
        if idx % 2 == 0:
            result.append(lst[idx])
        idx += 1
    return result

print(every_other([1,4,7,2,5])) # => [1,7,5]