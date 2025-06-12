# 0x08. Making Change

## Description

This project implements a solution to the classic "Making Change" problem using dynamic programming. Given a collection of coin denominations and a target amount, the algorithm determines the minimum number of coins needed to make that exact amount.

## Problem Statement

**Task 0: Change comes from within**

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount `total`.

### Requirements

- **Prototype**: `def makeChange(coins, total)`
- **Return**: Fewest number of coins needed to meet `total`
  - If `total` is `0` or less, return `0`
  - If `total` cannot be met by any number of coins you have, return `-1`
- **Parameters**:
  - `coins`: A list of the values of the coins in your possession
  - `total`: The target amount to make change for
- **Constraints**:
  - The value of a coin will always be an integer greater than `0`
  - You can assume you have an infinite number of each denomination of coin in the list
  - Your solution's runtime will be evaluated

## Algorithm Approach

This problem is solved using **Dynamic Programming** with the following approach:

1. **Base Cases**:
   - If `total ≤ 0`, return `0`
   - If no coins are provided, return `-1` (unless total is 0)

2. **Dynamic Programming Table**:
   - Create a DP array where `dp[i]` represents the minimum coins needed for amount `i`
   - Initialize `dp[0] = 0` (0 coins needed for amount 0)
   - Initialize all other positions to infinity (or a large number)

3. **Fill the DP Table**:
   - For each amount from 1 to `total`
   - For each coin denomination
   - If the coin value ≤ current amount, update: `dp[amount] = min(dp[amount], dp[amount - coin] + 1)`

4. **Return Result**:
   - If `dp[total]` is still infinity, return `-1` (impossible to make change)
   - Otherwise, return `dp[total]`

## Time and Space Complexity

- **Time Complexity**: O(total × number of coins)
- **Space Complexity**: O(total)

## Usage Example

```python
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))      # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
```

### Example Breakdown

**Example 1**: `makeChange([1, 2, 25], 37)`
- Target: 37
- Available coins: [1, 2, 25]
- Optimal solution: 25 + 25 = 50 is too much
- Better solution: 25 + 12×1 = 37 (13 coins)
- Even better: 25 + 6×2 = 37 (7 coins) ✓

**Example 2**: `makeChange([1256, 54, 48, 16, 102], 1453)`
- Target: 1453
- Available coins: [1256, 54, 48, 16, 102]
- No combination of these coins can sum to exactly 1453
- Return: -1

## File Structure

```
0x08-making_change/
├── README.md
├── 0-making_change.py    # Main implementation
└── 0-main.py            # Test file
```

## Repository Information

- **GitHub repository**: `alx-interview`
- **Directory**: `0x08-making_change`
- **File**: `0-making_change.py`

## Implementation Notes

- The solution must be efficient enough to handle large inputs
- Edge cases must be properly handled (zero/negative totals, impossible combinations)
- The algorithm assumes unlimited coins of each denomination
- Focus on optimizing runtime performance as it will be evaluated

## Testing

Run the test file to verify your implementation:

```bash
./0-main.py
```

Expected output:
```
7
-1
```

## Key Concepts

- **Dynamic Programming**: Breaking down the problem into smaller subproblems
- **Greedy vs Optimal**: This problem requires DP because greedy approach doesn't always work
- **Memoization**: Storing previously computed results to avoid redundant calculations
- **Bottom-up approach**: Building solution from smallest subproblems to the target

---

*This project is part of the ALX Software Engineering Program interview preparation track.*
