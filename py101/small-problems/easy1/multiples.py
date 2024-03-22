def multisum(cap):
    sums = 0
    for number in range(cap + 1):
        if number % 3 == 0 or number % 5 == 0:
            sums += number
    return sums

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)
