UNIT_CONVERSION = 10.7639

print("Please enter the width (m):")
width = float(input())
print("Please enter the length (m):")
length = float(input())

print(f"The room is {width * length} m^2 or {width * length * UNIT_CONVERSION} ft^2.")
