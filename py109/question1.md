> The code in `question1.py` contains two functions, `change_num_error()` and `change_num_fine(num)`. What does each function output, and what does printing `num` outside of the function(s) result in? Why does this behavior occur, and what concept(s) does this demonstrate?
---
## Key
### The answer should address the following:
1. `change_num_error()` results in an error (`UnboundLocalError`) because, when a variable is (re)assigned in a function definition, this creates a new local variable. This local variable is not initially assigned to anything, so reassigning it causes an error.
2. `change_num_fine(num)` prints `12`. This is because `num` is passed to the function as an argument. In this local scope, the local variable `num` shadows the global variable with the same name the scope of the function, meaning that the parameter `num` takes the object from the argument and assigns it to a local varibale.
3. `print(num)` outside of the function prints the global variable `num` as an output, which is `6`. This is because global variables that are not mutable collections cannot be modified in a local scope by (re)assignment.
4. This demonstrates the concepts of variable shadowing and Python's scoping rules regarding (re)assignment of variables within a local scope.
---
## Rubric
### The number of points for each element in the key is the following:
1. One point
2. One point
3. One point
4. Two points (describe both shadowing and reassignment in a local scope)
For a total of five points.
