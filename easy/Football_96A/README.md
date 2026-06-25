# Day 6 - Codeforces Solutions

## Problem 1: Football

### Problem
Given a string consisting of `0`s and `1`s representing players from two teams, determine whether there are **7 or more consecutive players** from the same team.

### Approach
- Traverse the string from left to right.
- Keep a count of consecutive identical characters.
- If the count reaches **7**, print `"YES"`.
- Otherwise, print `"NO"` after traversing the entire string.

### Algorithm
1. Read the input string.
2. Initialize `count = 1`.
3. Compare each character with the previous one.
4. If they are the same, increment `count`.
5. If `count >= 7`, output `"YES"` and terminate.
6. Otherwise, reset `count` to `1` when the character changes.
7. If no dangerous sequence is found, output `"NO"`.

### Complexity
- **Time:** `O(n)`
- **Space:** `O(1)`

### Key Concepts
- String Traversal
- Consecutive Character Counting
- Early Termination

---

