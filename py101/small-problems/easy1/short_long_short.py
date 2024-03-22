
def short_long_short(string1, string2):
    if len(string1) > len(string2):
        return string2 + string1 + string2
    if len(string2) > len(string1):
        return string1 + string2 + string1

# These examples should all print True
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")
