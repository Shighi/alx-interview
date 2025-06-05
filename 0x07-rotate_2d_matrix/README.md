# 0x07 - Rotate 2D Matrix

A Python implementation that rotates an n x n 2D matrix 90 degrees clockwise in-place.

## Table of Contents

- [Requirements](#requirements)
- [Project Description](#project-description)
- [Algorithm Overview](#algorithm-overview)
- [Implementation](#implementation)
- [Usage](#usage)
- [Examples](#examples)
- [Testing](#testing)
- [Files](#files)

## Requirements

### General
- **Allowed editors**: `vi`, `vim`, `emacs`
- **Environment**: Ubuntu 20.04 LTS using `python3` (version 3.8.10)
- **Code style**: `pycodestyle` (version 2.8.0)
- **File format**: All files should end with a new line
- **Shebang**: First line must be exactly `#!/usr/bin/python3`
- **Documentation**: All modules and functions must be documented
- **Permissions**: All files must be executable
- **Imports**: No external modules allowed
- **README**: This file is mandatory

## Project Description

This project implements a function that rotates a 2D matrix 90 degrees clockwise. The rotation is performed **in-place**, meaning the original matrix is modified directly without creating a new matrix.

### Key Constraints
- The matrix is guaranteed to be n x n (square matrix)
- The matrix will have 2 dimensions and will not be empty
- No return value - the matrix is edited in-place
- No external modules can be imported

## Algorithm Overview

To rotate a matrix 90 degrees clockwise in-place, we can use the following approach:

1. **Transpose the matrix**: Convert rows to columns
   - Element at position `[i][j]` moves to position `[j][i]`

2. **Reverse each row**: Flip each row horizontally
   - This completes the 90-degree clockwise rotation

### Mathematical Transformation
For a 90-degree clockwise rotation:
- Original position `[i][j]` → New position `[j][n-1-i]`

### Step-by-step Process
```
Original Matrix:    After Transpose:    After Row Reverse:
[1, 2, 3]          [1, 4, 7]           [7, 4, 1]
[4, 5, 6]    →     [2, 5, 8]     →     [8, 5, 2]
[7, 8, 9]          [3, 6, 9]           [9, 6, 3]
```

## Implementation

The solution implements the `rotate_2d_matrix(matrix)` function that:
- Takes an n x n 2D matrix as input
- Modifies the matrix in-place to achieve 90-degree clockwise rotation
- Returns nothing (void function)

### Function Signature
```python
def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in-place.
    
    Args:
        matrix (list[list[int]]): The n x n 2D matrix to rotate
        
    Returns:
        None: The matrix is modified in-place
    """
```

## Usage

### Basic Usage
```python
#!/usr/bin/python3
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

# Create a 3x3 matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Rotate the matrix 90 degrees clockwise
rotate_2d_matrix(matrix)

# Print the rotated matrix
print(matrix)
# Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```

### Running the Example
```bash
$ chmod +x main_0.py 0-rotate_2d_matrix.py
$ ./main_0.py
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

## Examples

### Example 1: 3x3 Matrix
```python
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotate_2d_matrix(matrix)
# Result: [[7, 4, 1],
#          [8, 5, 2],
#          [9, 6, 3]]
```

### Example 2: 4x4 Matrix
```python
matrix = [[1,  2,  3,  4],
          [5,  6,  7,  8],
          [9,  10, 11, 12],
          [13, 14, 15, 16]]

rotate_2d_matrix(matrix)
# Result: [[13, 9,  5, 1],
#          [14, 10, 6, 2],
#          [15, 11, 7, 3],
#          [16, 12, 8, 4]]
```

### Example 3: 2x2 Matrix
```python
matrix = [[1, 2],
          [3, 4]]

rotate_2d_matrix(matrix)
# Result: [[3, 1],
#          [4, 2]]
```

### Example 4: 1x1 Matrix
```python
matrix = [[42]]

rotate_2d_matrix(matrix)
# Result: [[42]]  # No change for 1x1 matrix
```

## Testing

### Test File Structure
Create a test file to verify the implementation:

```python
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

def test_rotate_matrix():
    # Test 3x3 matrix
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    
    rotate_2d_matrix(matrix)
    expected = [[7, 4, 1],
                [8, 5, 2],
                [9, 6, 3]]
    
    assert matrix == expected, f"Expected {expected}, got {matrix}"
    print("3x3 matrix test passed!")

if __name__ == "__main__":
    test_rotate_matrix()
```

### Running Tests
```bash
$ chmod +x test_rotate.py
$ ./test_rotate.py
3x3 matrix test passed!
```

## Files

### Project Structure
```
0x07-rotate_2d_matrix/
├── README.md                 # This documentation file
├── 0-rotate_2d_matrix.py    # Main implementation file
└── main_0.py                # Test/example file
```

### File Descriptions

- **`0-rotate_2d_matrix.py`**: Contains the main `rotate_2d_matrix()` function implementation
- **`main_0.py`**: Example usage and test case
- **`README.md`**: Project documentation (this file)

### File Requirements
- All Python files start with `#!/usr/bin/python3`
- All files are executable (`chmod +x filename`)
- Code follows `pycodestyle` standards
- All functions include proper documentation

## Algorithm Complexity

- **Time Complexity**: O(n²) where n is the dimension of the matrix
  - We need to visit each element once for transpose and once for row reversal
- **Space Complexity**: O(1) 
  - The rotation is performed in-place with no additional data structures

## Repository Information

- **GitHub repository**: `alx-interview`
- **Directory**: `0x07-rotate_2d_matrix`
- **Main file**: `0-rotate_2d_matrix.py`

## Additional Notes

This implementation is part of the ALX interview preparation curriculum, focusing on:
- In-place matrix manipulation
- Understanding 2D array transformations
- Implementing algorithms without external dependencies
- Code optimization and space efficiency

The solution demonstrates fundamental concepts in:
- Matrix mathematics
- In-place algorithms
- Python list manipulation
- Algorithm optimization
