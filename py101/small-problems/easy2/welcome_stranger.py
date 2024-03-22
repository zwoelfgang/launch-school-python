def greetings(lst, dct):
    return f"Hello, {' '.join(lst)}! Nice to have a {dct['title']} {dct['occupation']} around."

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.