# A. Circle of Apple Trees

**Platform:** Codeforces  
**Problem:** A. Circle of Apple Trees  
**Language:** Python 3  
**Topics:** Arrays, Sets, Greedy, Implementation

## Problem Summary

There are `n` apple trees arranged in a circle. Each tree has one apple with a given beauty value.

We start at the first tree and can move around the circle indefinitely.

An apple can only be eaten if its beauty is strictly greater than the beauty of the previously eaten apple.

We can also skip apples and eat them during subsequent rounds.

The objective is to maximize the number of apples we can eat.

## Approach: Counting Distinct Elements

The important observation is that the position of an apple does not matter because we can travel around the circle multiple times.

We can skip apples until we encounter an apple with the next required beauty value.

However, we cannot eat two apples with the same beauty because the beauty must strictly increase.

Therefore, the maximum number of apples we can eat equals the number of distinct beauty values.

### Algorithm

1. Read the number of test cases.
2. For each test case, read `n` and the beauty array.
3. Convert the array into a Python set using `set(b)`.
4. Count the distinct elements using `len()`.
5. Print the result.

## Python Code

```python
t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))

    print(len(set(b)))
```

## Complexity Analysis

- **Time Complexity:** O(n) average per test case for constructing the set.
- **Space Complexity:** O(n) for storing distinct elements.

## Key Learnings

- Python sets automatically remove duplicate elements.
- Circular traversal allows us to skip elements and revisit trees.
- Strictly increasing sequences cannot contain duplicate values.
- Mathematical observations can eliminate unnecessary simulations.

## Conclusion

This problem demonstrates how understanding the constraints and identifying the key observation can turn a seemingly complex circular traversal problem into a simple set operation.