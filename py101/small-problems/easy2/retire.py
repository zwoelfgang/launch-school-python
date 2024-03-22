import datetime

age = int(input("What is your age? "))
retirement_age = int(input("At what age would you like to retire? "))

print(f"It's {datetime.datetime.today().year}. You will retire in {(retirement_age - age) + datetime.datetime.today().year}.")
print(f"You have only {retirement_age - age} years of work to go!")
