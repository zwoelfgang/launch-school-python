> The code in `question3.py` contains a dictionary with a string as each key and a tuple for each value. What does the function do, or not do, to the dictionary such that the print statement prints what it does and why? What concept(s) does this demonstrate?
---
## Key
### The answer should address the following:
1. The function `change_dictionary()` is not passed in the global variable `dictionary` as an argument, but the print statement after function invocation prints the dictionary with *new* tuples as values representing the first element in each being converted to strings.
2. The dictionary is a mutable collection, so even though the value tuples are immutable, they are replaced by new tuple objects and that is why printing the global variable after the function invocation prints the mutated dictionary.
---
## Rubric
### The number of points for each element in the key is the following:
1. Two points (for specifying what is printed and what the function did)
2. Two points (for specifying mutability as the concept and that the objects are replaced in this instance)
