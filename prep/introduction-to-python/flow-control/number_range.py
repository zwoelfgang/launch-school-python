def number_range(num):
    if 0 <= num <= 50:
        print(f"{num} is between 0 and 50")
    elif 51 <= num <= 100:
        print(f"{num} is between 51 and 100")
    elif num >= 100:
        print(f"{num} is greater than 100")
    else:
        print(f"{num} is less than 0")

number = int(input("Enter a number: "))

number_range(number)
