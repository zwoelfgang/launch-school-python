lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

removed_items = [sublist.remove(item) for sublist in lst 
                                  for item in sublist if item % 3 != 0]
print(lst)
