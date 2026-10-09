# Binary Array Game

## Problem Description

Alice and Bob play a game on a binary array of size `n`, containing only `0`s and `1`s. Alice moves first, and the players alternate turns.

On each turn, a player selects a subarray of length at least two and replaces it with a single element:

- If every element in the selected subarray is `1`, it is replaced with `0`.
- Otherwise, it is replaced with `1`.

The game ends when only one element remains. Alice wins if the final element is `0`; otherwise, Bob wins.

## Approach

Check the first and last elements of the array.

- If both endpoints are `0`, print `Bob`.
- Otherwise, print `Alice`.

## Python Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if a[0] == 0 and a[-1] == 0:
        print("Bob")
    else:
        print("Alice")
```

## Complexity Analysis

- **Time Complexity:** `O(n)` per test case for reading the array.
- **Space Complexity:** `O(n)` for storing the array.

## Key Learning

This problem demonstrates how identifying a simple pattern in the initial array can eliminate the need to simulate every move in a game.
