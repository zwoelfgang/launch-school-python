string = 'launch school tech & talk'

lst = [char for char in string]
idx = 0

while idx < len(lst):
    if idx == 0 or lst[idx - 1] == ' ':
        lst[idx] = lst[idx].capitalize()
    idx += 1

string = ''.join(lst)
print(string)
