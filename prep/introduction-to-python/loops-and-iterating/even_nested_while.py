my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

i = 0
j = 0

while i < len(my_list):
    while j < len(my_list[i]):
        if my_list[i][j] % 2 == 0:
            print(my_list[i][j])
        j += 1
    i += 1
    j = 0
