# Pascal's Triangle

This project implements a function that generates Pascal's Triangle up to n rows. Pascal's Triangle is a triangular array of numbers where each number is the sum of the two numbers directly above it.

## Description

In this project, we implement a Python function `pascal_triangle(n)` that returns a list of lists of integers representing Pascal's Triangle up to the nth row.

Pascal's Triangle has the following properties:
- The first row is always `[1]`
- Each subsequent row starts and ends with 1
- Every other value is the sum of the two values directly above it

For example, the first 5 rows of Pascal's Triangle are:
```
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
```

## Requirements

### General
- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable
- The length of your files will be tested using `wc`

## Task 0: Pascal's Triangle

Write a function `def pascal_triangle(n):` that returns a list of lists of integers representing Pascal's Triangle of n:
- Returns an empty list if `n <= 0`
- You can assume `n` will always be an integer

Example:
```python
def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

print_triangle(pascal_triangle(5))
```

Output:
```
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```

## Key Concepts to Know

To successfully complete this project, you should understand:

1. **Lists and List Comprehensions**
2. **Functions and Return Values**
3. **Iterative Control Flow (Loops)**
4. **Conditional Statements**
5. **Recursion (Optional Approach)**
6. **Arithmetic Operations**
7. **Indexing and Slicing of Lists**
8. **Memory Management**
9. **Error and Exception Handling**
10. **Algorithm Efficiency and Optimization**

## Files

- **0-pascal_triangle.py**: Contains the implementation of the `pascal_triangle(n)` function

## Author

Shighi