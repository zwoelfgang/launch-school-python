stuff = ('hello', 'world', 'bye', 'now')

list_stuff = list(stuff)
list_stuff[2] = 'goodbye'
stuff = tuple(list_stuff)

print(stuff)
