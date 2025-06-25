# Prime Game

A competitive game theory problem involving strategic removal of prime numbers and their multiples from a set of consecutive integers. This project implements an optimal solution to determine the winner between two players (Maria and Ben) across multiple rounds of the game.

## 🎮 Game Rules

Maria and Ben play a game with the following rules:
1. Given a set of consecutive integers from 1 to n (inclusive)
2. Players take turns choosing a prime number from the set
3. When a prime is chosen, both the prime and all its multiples are removed from the set
4. The player who cannot make a move (no primes left) loses the round
5. Maria always goes first
6. Both players play optimally

## 🧮 Mathematical Concepts

### Prime Numbers
- Numbers greater than 1 that have no positive divisors other than 1 and themselves
- Essential for determining valid moves in each game round

### Sieve of Eratosthenes
- Efficient algorithm for finding all prime numbers up to a given limit
- Time complexity: O(n log log n)
- Used to precompute primes for optimization

### Game Theory
- **Optimal Play**: Both players make the best possible moves
- **Win Conditions**: Player unable to move loses
- **Strategic Analysis**: Determining winner based on game state

### Dynamic Programming
- Memoization of game outcomes for different values of n
- Optimization technique to avoid recalculating results
- Essential for handling multiple rounds efficiently

## 🎯 Problem Analysis

The key insight is that the winner depends on the **number of prime numbers** available:
- If the count of primes ≤ n is **odd**, Maria wins (she goes first)
- If the count of primes ≤ n is **even**, Ben wins
- The winner is determined by who has the most round victories

## 🚀 Algorithm Strategy

1. **Precompute Primes**: Use Sieve of Eratosthenes to find all primes up to the maximum possible n
2. **Count Primes**: For each n, count the number of primes ≤ n
3. **Determine Winner**: Use the parity of prime count to determine round winner
4. **Aggregate Results**: Count wins for each player across all rounds

## 📁 Project Structure

```
0x0A-primegame/
├── 0-prime_game.py    # Main implementation
├── main_0.py          # Test file
└── README.md          # This file
```

## 🔧 Implementation

### Function Signature
```python
def isWinner(x, nums):
    """
    Determines the winner of the prime game.
    
    Args:
        x (int): Number of rounds
        nums (list): Array of n values for each round
    
    Returns:
        str: Name of the player with most wins ("Maria" or "Ben")
        None: If winner cannot be determined (tie)
    """
```

### Algorithm Steps
1. Handle edge cases (invalid input)
2. Find maximum n to determine sieve range
3. Generate primes using Sieve of Eratosthenes
4. Count primes for each possible n value
5. Simulate each game round
6. Return player with most victories

## 📊 Example Walkthrough

**Input**: `x = 3, nums = [4, 5, 1]`

### Round 1: n = 4
- Initial set: {1, 2, 3, 4}
- Primes available: {2, 3}
- Maria picks 2, removes {2, 4} → {1, 3}
- Ben picks 3, removes {3} → {1}
- **Ben wins** (Maria cannot move)

### Round 2: n = 5
- Initial set: {1, 2, 3, 4, 5}
- Primes available: {2, 3, 5}
- Maria picks 2, removes {2, 4} → {1, 3, 5}
- Ben picks 3, removes {3} → {1, 5}
- Maria picks 5, removes {5} → {1}
- **Maria wins** (Ben cannot move)

### Round 3: n = 1
- Initial set: {1}
- No primes available
- **Ben wins** (Maria cannot move)

**Result**: Ben wins 2 rounds, Maria wins 1 round → **Ben**

## 💻 Usage

### Basic Usage
```python
#!/usr/bin/python3
from prime_game import isWinner

# Test the function
result = isWinner(3, [4, 5, 1])
print(f"Winner: {result}")  # Output: Winner: Ben
```

### Running the Test
```bash
chmod +x main_0.py
./main_0.py
```

## ⚡ Performance Optimization

### Time Complexity
- **Sieve Generation**: O(max(nums) * log log max(nums))
- **Prime Counting**: O(max(nums))
- **Game Simulation**: O(x)
- **Overall**: O(max(nums) * log log max(nums) + x)

### Space Complexity
- O(max(nums)) for storing sieve and prime counts

### Optimization Techniques
1. **Precomputation**: Calculate all primes once using sieve
2. **Memoization**: Store prime counts for reuse
3. **Early Termination**: Handle edge cases efficiently
4. **Batch Processing**: Process all rounds after setup

## 🧪 Test Cases

```python
# Test Case 1: Basic functionality
assert isWinner(3, [4, 5, 1]) == "Ben"

# Test Case 2: Maria wins majority
assert isWinner(2, [3, 7]) == "Maria"

# Test Case 3: Tie scenario
assert isWinner(2, [2, 4]) == None

# Test Case 4: Edge case - single round
assert isWinner(1, [10]) == "Maria"

# Test Case 5: Large numbers
assert isWinner(5, [2, 5, 1, 4, 3]) == "Ben"
```

## 🔍 Key Insights

1. **Prime Count Parity**: The winner is determined by whether the number of primes is odd or even
2. **Optimal Strategy**: Both players will always choose optimally, making the game deterministic
3. **Efficiency**: Precomputing primes allows for O(1) lookup during game simulation
4. **Edge Cases**: Handle scenarios with no primes, ties, and invalid inputs

## 📋 Requirements

- **Python Version**: 3.4.3+
- **Operating System**: Ubuntu 20.04 LTS
- **Code Style**: PEP 8 compliant
- **Constraints**: 
  - No external packages allowed
  - n and x ≤ 10,000
  - All files must be executable

## 🎓 Learning Outcomes

After completing this project, you'll understand:

- **Prime Number Theory**: Efficient prime generation and properties
- **Algorithm Optimization**: Using sieves and memoization for performance
- **Game Theory**: Analyzing competitive scenarios and optimal strategies
- **Dynamic Programming**: Caching results for improved efficiency
- **Python Proficiency**: Advanced list manipulation and algorithmic thinking

## 📚 Resources

### Mathematical Concepts
- [Khan Academy: Prime Numbers](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratic-functions-equations/x2f8bb11595b61c86:quadratic-equations-factoring/a/prime-numbers)
- [Sieve of Eratosthenes Algorithm](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)

### Game Theory
- [Game Theory Basics](https://www.investopedia.com/terms/g/gametheory.asp)
- [Optimal Play Strategies](https://brilliant.org/wiki/game-theory/)

### Programming Resources
- [Python Official Documentation](https://docs.python.org/3/)
- [Dynamic Programming Guide](https://www.geeksforgeeks.org/dynamic-programming/)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)

## 🏆 Success Tips

1. **Understand the Pattern**: Focus on the relationship between prime count and winner
2. **Optimize Early**: Use efficient algorithms from the start
3. **Test Thoroughly**: Verify your solution with multiple test cases
4. **Handle Edge Cases**: Consider scenarios with small numbers and ties
5. **Code Cleanly**: Follow PEP 8 standards for maintainable code

---
