# Codeforces - A. Shashliks

## Problem Statement

You are given an initial grill temperature `k` and two types of shashliks.

- Type 1 requires a temperature of at least `a` and decreases the temperature by `x`.
- Type 2 requires a temperature of at least `b` and decreases the temperature by `y`.

The grill temperature can become negative.

The task is to determine the maximum total number of shashlik portions that can be cooked.

## Approach: Greedy + Trying Both Orders

The order of cooking matters because each portion decreases the grill temperature.

We consider both possible cooking orders:

1. Cook Type 1 as many times as possible, then cook Type 2.
2. Cook Type 2 as many times as possible, then cook Type 1.

For each type, calculate the maximum number of portions that can be cooked using:

\[
count = \left\lfloor\frac{k-required}{drop}\right\rfloor+1
\]

This formula is used only when the current temperature is at least the required temperature. Otherwise, the count is zero.

After cooking a type, update the temperature:

\[
k = k - (count \times drop)
\]

Finally, return the maximum total from the two orders.

## Python 3 Solution

```python
def cook(k, required, drop):
    if k < required:
        return 0, k

    count = (k - required) // drop + 1
    k -= count * drop

    return count, k


t = int(input())

for _ in range(t):
    k, a, b, x, y = map(int, input().split())

    # Type 1 followed by Type 2
    count1, temp1 = cook(k, a, x)
    count2, temp2 = cook(temp1, b, y)
    total1 = count1 + count2

    # Type 2 followed by Type 1
    count3, temp3 = cook(k, b, y)
    count4, temp4 = cook(temp3, a, x)
    total2 = count3 + count4

    print(max(total1, total2))
```

## Example

**Input:**

```text
5
10 3 4 2 1
1 10 10 1 1
100 17 5 2 3
28 14 5 2 4
277 5 14 1 3
```

**Output:**

```text
8
0
46
10
273
```

## Complexity Analysis

- **Time Complexity:** O(1) per test case because only two cooking orders are evaluated.
- **Space Complexity:** O(1) because only a few variables are used.

## Key Learnings

- Applying greedy strategies to optimization problems.
- Understanding how operation order affects the result.
- Using integer division to calculate the maximum number of possible operations.
- Comparing multiple possible strategies to find the optimal answer.

---

**Problem:** A. Shashliks  
**Platform:** Codeforces  
**Language:** Python 3