statement = "The Flintstones Rock"

char_freq = {}
statement = statement.replace(' ', '')
for char in statement:
    char_freq[char] = char_freq.get(char, 0) + 1

print(char_freq)
