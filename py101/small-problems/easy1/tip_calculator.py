bill = float(input("What is the bill?\n"))
tip = float(input("What is the tip percentage?\n"))

print(f"The tip is ${((tip / 100) * bill):.2f}")
print(f"The total is ${(((tip / 100) * bill) + bill):.2f}")