# C. Pacer

**Platform:** Codeforces  
**Problem:** C. Pacer  
**Difficulty:** 1300  
**Topic:** Greedy, Mathematics, Parity  
**Language:** Python 3

## Problem Statement

Farmer John runs between two sides of a gym. Each time he runs to the opposite side, he earns 1 point. He can also stay at his current position without earning points.

There are `m` minutes in total. At specific minutes `a[i]`, he must be at side `b[i]`.

The task is to maximize the total points while satisfying all position requirements.

## Approach: Greedy + Parity

For every requirement, calculate:

- `duration = a - prev_time`: Number of available minutes.
- `required_moves = abs(b - prev_side)`: Minimum moves needed to reach the required side.

Since each run changes the current side, the parity of the number of runs determines the final side.

**Greedy Strategy:**

1. If `(duration - required_moves) % 2 == 0`, FJ can run during every available minute.
2. Otherwise, he must stay for one minute to satisfy the required position.
3. Update the previous time and side.
4. After processing all requirements, add all remaining minutes to the answer.

## Python Solution

```python
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    prev_time = 0
    prev_side = 0
    ans = 0

    for _ in range(n):
        a, b = map(int, input().split())

        duration = a - prev_time
        required_moves = abs(b - prev_side)

        if (duration - required_moves) % 2 == 0:
            ans += duration
        else:
            ans += duration - 1

        prev_time = a
        prev_side = b

    ans += m - prev_time

    print(ans)
```

## Complexity Analysis

| Complexity | Value | Explanation |
| Time | O(n) | Each requirement is processed once. |
| Space | O(1) | Only a constant number of variables are used. |

## Key Concepts Learned

- Greedy Algorithms
- Parity (Even and Odd)
- Mathematical Observation
- State Tracking
- Optimal Movement Decisions

## Conclusion

The problem can be solved efficiently using a greedy approach and parity checking. Instead of exploring every possible movement, we calculate whether all available minutes can be used for running or whether one minute must be sacrificed.

**Time Complexity: O(n)**  
**Space Complexity: O(1)**
