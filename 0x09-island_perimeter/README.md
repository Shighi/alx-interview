# 0x09. Island Perimeter

## Description
This project focuses on solving the island perimeter problem using Python. The task involves calculating the perimeter of an island represented in a 2D grid where 1s represent land and 0s represent water.

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Code should use the `PEP 8` style (version 1.7)
- You are not allowed to import any module
- All modules and functions must be documented
- All files must be executable

## Tasks

### 0. Island Perimeter
**File:** `0-island_perimeter.py`

Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in `grid`.

**Specifications:**
- `grid` is a list of list of integers:
  - `0` represents water
  - `1` represents land
  - Each cell is square, with a side length of 1
  - Cells are connected horizontally/vertically (not diagonally)
  - `grid` is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing)
- The island doesn't have "lakes" (water inside that isn't connected to the water surrounding the island)

**Example:**
```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12
```

## Algorithm Approach

The solution involves iterating through each cell in the grid and for every land cell (1), checking its four adjacent cells (up, down, left, right). The perimeter increases by 1 for each adjacent cell that is either water (0) or out of bounds.

## Usage

```bash
chmod +x 0-island_perimeter.py
./0-main.py
```

## Repository Information
- **GitHub repository:** `alx-interview`
- **Directory:** `0x09-island_perimeter`
- **Files:** 
  - `README.md`
  - `0-island_perimeter.py`

## Author
ALX Software Engineering Program - Interview Preparation

## License
This project is part of the ALX Software Engineering curriculum.
