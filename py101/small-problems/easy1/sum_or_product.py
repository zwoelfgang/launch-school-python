integer = int(input("Please enter an integer greater than 0: "))
string = input("Enter \"s\" to compute the sum, or \"p\" to compute the product: ")

sum = 0
product = 1

if string == 's':
    for num in range(1, integer + 1):
        sum += num
    print(f"The sum of the integers between 1 and {integer} is {sum}.")
elif string == 'p':
    for num in range(1, integer + 1):
        product *= num
    print(f"The product of the integers between 1 and {integer} is {product}.")
