# B. The Secret Number

**Platform:** Codeforces  
**Problem:** B. The Secret Number  
**Language:** Python 3  
**Topics:** Mathematics, Number Theory, Implementation

## Problem Summary

Vadim thinks of a positive integer `x` and appends a positive number of zeros to its right.

The resulting number is added to the original number to obtain the given integer `n`.

Our task is to find all possible original numbers `x` in ascending order.

## Approach: Mathematical Observation

Let:
- `x` be the original number.
- `k` be the number of appended zeros.
- `10^k` represent the multiplier after appending zeros.

The resulting number is:

`x * 10^k`

According to the problem:

`n = x + x * 10^k`

Taking `x` common:

`n = x * (10^k + 1)`

Therefore:

`x = n / (10^k + 1)`

### Algorithm

1. Read the number of test cases.
2. For each test case, initialize an empty answer list.
3. Start with `p = 10`, representing one appended zero.
4. Check whether `n` is divisible by `p + 1`.
5. If divisible, calculate `x = n // (p + 1)` and store it.
6. Multiply `p` by 10 to check the next possible number of zeros.
7. Sort the answers in ascending order.
8. Print the count and all suitable numbers.

## Python Code

```python
t = int(input())

for _ in range(t):
    n = int(input())
    ans = []

    p = 10

    while p + 1 <= n:
        if n % (p + 1) == 0:
            ans.append(n // (p + 1))

        p *= 10

    ans.sort()

    print(len(ans), *ans)
```

## Complexity Analysis

**Time Complexity:** O(log n)

We check powers of 10 until they exceed the given number. Sorting the resulting answers also takes O(log n log log n) in the worst case, which is dominated by O(log n) for this problem's bounded number of candidates.

**Space Complexity:** O(log n) for storing valid answers.

## Key Learnings

- Appending zeros is equivalent to multiplying by a power of 10.
- Mathematical equations can simplify brute-force searches.
- Divisibility checks help identify valid candidates.
- Python integers support large values without integer overflow.

## Conclusion

This problem demonstrates how mathematical observation and divisibility can replace unnecessary brute-force generation.