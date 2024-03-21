num = 6

def change_num_error():
    num += num
    print(num)

def change_num_fine(num):
    num += num
    print(num)

change_num_fine(num)
print(num)
# What will happen with change_num_error()?
