# 0x01. Lockboxes

## Description
This project focuses on solving the Lockboxes problem, which is a common algorithmic interview question. The challenge involves determining if all boxes in a set can be unlocked based on the keys contained within them.

## Additional Resources
* Mock Technical Interview

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

### 0. Lockboxes (mandatory)

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

* Prototype: `def canUnlockAll(boxes)`
* `boxes` is a list of lists
* A key with the same number as a box opens that box
* You can assume all keys will be positive integers
  * There can be keys that do not have boxes
* The first box `boxes[0]` is unlocked
* Return `True` if all boxes can be opened, else return `False`

#### Example

```python
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Output: False
```

## Algorithm Approach

To solve this problem, we need to:
1. Keep track of which boxes are unlocked
2. Keep track of which keys we have available
3. Start with box 0 (which is already unlocked)
4. For each unlocked box, collect all the keys inside
5. Use the collected keys to unlock more boxes
6. Repeat until no more boxes can be unlocked
7. Check if all boxes are unlocked

This can be implemented using various approaches such as:
- Depth-First Search (DFS)
- Breadth-First Search (BFS)
- Iterative approach with a stack or queue

## Repository Information
* GitHub repository: `alx-interview`
* Directory: `0x01-lockboxes`
* File: `0-lockboxes.py`
