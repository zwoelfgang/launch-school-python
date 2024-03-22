> What does the code in `question2.py` do to the list variable `lst`? Why does this behavior occur and what concept(s) does this code demonstrate?
---
## Key
### The answer should address the following:
1. When the function `populate_list()` is called, the `.append()` method is applied to the list, which adds an object to the list at the last index within the list object.
2. Printing the list `lst` after calling the function prints the list containing the new element `['Hi']`, even though this list was not passed into the function as an argument.
3. The reason printing the list after calling the function `populate_list()` results in `['Hi']` is that lists are mutable, and may have objects contained within that can be changed. In this case the variable used is the global variable `lst`, due to using the `.append()` method which mutates lists in place by adding a new object.
---
## Rubric
### The number of points for each element in the key is the following:
1. One point
2. One point
3. One point
For a total of three points.
