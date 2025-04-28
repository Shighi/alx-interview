# 0x02. Minimum Operations

## Description
This project tackles an algorithmic problem related to text editing operations. Given a single character 'H' in a text file and two available operations: 'Copy All' and 'Paste', the challenge is to calculate the minimum number of operations required to obtain exactly 'n' 'H' characters in the file.

## Requirements

### General
* Allowed editors: `vi`, `vim`, `emacs`
* All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
* All files should end with a new line
* The first line of all files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should be documented
* Your code should use the `PEP 8` style (version 1.7.x)
* All files must be executable

## Tasks

### 0. Minimum Operations (mandatory)

In a text file, there is a single character `H`. Your text editor can execute only two operations in this file:
- `Copy All`: Copies all the characters currently in the file.
- `Paste`: Pastes the characters that were previously copied.

Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file.

* Prototype: `def minOperations(n)`
* Returns an integer
* If `n` is impossible to achieve, return `0`

#### Example:
For `n = 9`:
1. Start with one character: `H`
2. `Copy All` (operation 1)
3. `Paste` → `HH` (operation 2)
4. `Paste` → `HHH` (operation 3)
5. `Copy All` (operation 4)
6. `Paste` → `HHHHHH` (operation 5)
7. `Paste` → `HHHHHHHHH` (operation 6)

Total number of operations: `6`

#### Test Case:
```python
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
```

#### Expected Output:
```
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
```

## Approach
This problem can be understood by recognizing that the most efficient way to build up 'n' characters is to find factors of 'n' and use them strategically. The key insights are:

1. For prime numbers, we need to copy the initial 'H' and then paste it (n-1) times.
2. For composite numbers, we can break down the problem based on the prime factorization of 'n'.
3. The minimum operations will be the sum of all prime factors of 'n'.

For example, with n=12:
- 12 = 2 × 2 × 3
- So the minimum operations = 2 + 2 + 3 = 7

## Repository
* GitHub repository: `alx-interview`
* Directory: `0x02-minimum_operations`
* File: `0-minoperations.py`
