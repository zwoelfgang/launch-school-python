def starts_with(string, prefix):
    return True if string.find(prefix) == 0 else False

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True
