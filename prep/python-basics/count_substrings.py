def count_substrings(string, substring):
    counter = 0
    idx = 0
    while string[idx:].find(substring) != -1:
        counter += 1
        idx += len(substring) + string[idx:].find(substring)
    return counter
        

print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0
