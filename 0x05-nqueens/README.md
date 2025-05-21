# N Queens Problem

## Description

This project contains a Python script that solves the N Queens problem using the backtracking algorithm. The N Queens problem is the challenge of placing N non-attacking queens on an N x N chessboard.

A queen is said to be attacking another queen if it is on the same row, column, or diagonal. The objective is to place N queens on the board such that no two queens attack each other.

## Files

* `0-nqueens.py`: The main script that solves the N Queens problem.

## Usage

To run the program, use the following command:

```
./0-nqueens.py N
```

* `N` must be an integer greater than or equal to 4.
* If `N` is not an integer or is less than 4, the script will print an error message and exit with status 1.

### Examples

```
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

## Requirements

* Allowed editors: `vi`, `vim`, `emacs`
* Files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
* All Python files must:

  * Begin with `#!/usr/bin/python3`
  * End with a new line
  * Be executable
  * Follow PEP 8 style (version 1.7.\*)
* Only the `sys` module is allowed for import

## Author

Daisy Mwambi

## Repository

* GitHub: [alx-interview](https://github.com/Shighi/alx-interview)
* Directory: `0x05-nqueens`
* File: `0-nqueens.py`

