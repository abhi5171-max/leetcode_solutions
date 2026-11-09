# A. Homework

**Platform:** Codeforces  
**Problem:** A. Homework  
**Language:** Python 3  
**Topics:** Strings, Implementation, Greedy

## Problem Summary

Vlad and Dima are given two strings `a` and `b`.

They must add all characters of `b` to `a` in their original order.

There are two rules:

- Vlad (`V`) adds a character to the beginning of the string.
- Dima (`D`) adds a character to the end of the string.

The task is to determine the final resulting string.

## Approach: String Manipulation

Instead of modifying the original string after every operation, maintain two separate strings:

- `left`: Stores characters added by Vlad.
- `right`: Stores characters added by Dima.

### Algorithm

1. Read the number of test cases.
2. Read the initial string `a`.
3. Read strings `b` and `c`.
4. Initialize two empty strings: `left` and `right`.
5. Iterate through every character of `b`.
6. If the corresponding character in `c` is `V`, prepend the character to `left`.
7. Otherwise, append the character to `right`.
8. Combine `left + a + right` and print the result.

## Python Code

```python
t = int(input())

for _ in range(t):
    n = int(input())
    a = input()

    m = int(input())
    b = input()
    c = input()

    left = ""
    right = ""

    for i in range(m):
        if c[i] == 'V':
            left = b[i] + left
        else:
            right += b[i]

    print(left + a + right)
```

## Complexity Analysis

- **Time Complexity:** O(m²) with Python string concatenation in the worst case, where `m` is the length of string `b`.
- **Space Complexity:** O(m) for storing the additional characters.

Since `m <= 10`, this solution easily satisfies the constraints.

## Key Learnings

- String manipulation using concatenation.
- Understanding prefix and suffix insertion.
- Processing characters in their original order.
- Maintaining separate strings to simplify implementation.

## Conclusion

This problem demonstrates how a simple string manipulation strategy can avoid repeatedly modifying the original string.