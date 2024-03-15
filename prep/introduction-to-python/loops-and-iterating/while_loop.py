my_list = [6, 3, 0, 11, 20, 4, 17]

i = 0
k = 0

print("While loop:")

while i < len(my_list):
    print(my_list[i])
    i += 1

print("For loop:")

for j in my_list:
    print(j)

print("While even:")

while k < len(my_list):
    if (my_list[k] % 2 == 0):
        print(my_list[k])
    k += 1

print("For odd:")

for l in my_list:
    if l % 2 == 1:
        print(l)
