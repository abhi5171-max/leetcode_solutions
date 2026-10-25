# A. Round Trip

**Platform:** Codeforces  
**Problem:** A. Round Trip  
**Language:** Python 3  
**Topics:** Greedy, Implementation, Strings

## Problem Statement

Vasya participates in a sequence of Codeforces rounds. There are two types of rounds:

- **Div. 1 (`1`):** Always rated.
- **Div. 2 (`2`):** Rated only when Vasya's rating is strictly less than `x`.

Given Vasya's initial rating `a`, threshold `x`, maximum rating change `k`, and a string representing the rounds, determine the maximum number of rated rounds he can participate in.

## Approach

Use a greedy strategy to maximize the number of rated rounds.

1. Iterate through the rounds in order.
2. For a Div. 1 round, increment the answer because it is always rated.
3. For a Div. 2 round, increment the answer only if the current rating is less than `x`.
4. After each rated round, choose a rating decrease of up to `k` to help qualify for future Div. 2 rounds, without allowing the rating to become negative.

## Python Solution

```python
t = int(input())

for _ in range(t):
    a, x, k, n = map(int, input().split())
    s = input().strip()

    ans = 0

    for c in s:
        if c == '1':
            ans += 1
            a = max(0, a - k)
        else:
            if a < x:
                ans += 1
                a = max(0, a - k)

    print(ans)
```

## Example

**Input

```text
4
2100 2100 5 3
222
2098 2100 5 6
111211
2115 2100 226 7
2211121
0 10 4 8
22111121
```

**Output

```text
0
6
5
8
```

## Complexity Analysis

- **Time Complexity:** `O(n)` per test case, where `n` is the number of rounds.
- **Space Complexity:** `O(n)` for storing the round string.

## Key Learning

This problem demonstrates greedy decision-making: reduce the rating strategically after rated rounds to maximize eligibility for subsequent Div. 2 rounds.
