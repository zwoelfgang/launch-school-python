def all_caps(text):
    if len(text) > 10:
        return text.upper()
    else:
        return text
    
string = 'hello world'
farewell = 'goodbye'

print(all_caps(string))
print(all_caps(farewell))
