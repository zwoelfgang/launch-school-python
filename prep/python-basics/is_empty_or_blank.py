def is_empty_or_blank(string):
    return True if ((not string) or string.isspace()) else False

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True
