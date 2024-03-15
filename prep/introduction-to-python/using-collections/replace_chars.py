info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

text = list(info)
j = 0

for i in text:
    if i == ':':
        text[j] = '+'
    j += 1

info = "".join(text)
print(info)
