# B. Blackslex and Showering

## Problem Description

Blackslex needs to visit several floors in a specific order. The total time taken is the sum of the absolute differences between consecutive floor numbers.

He can skip visiting **at most one floor**. The task is to find the minimum possible total time after removing zero or one element from the array.

## Approach: Greedy Algorithm

1. Calculate the original total time by summing the absolute differences between consecutive elements.
2. Consider removing each element:
   - **First element:** Subtract the difference between the first and second elements.
   - **Last element:** Subtract the difference between the last and second-last elements.
   - **Middle element:** Remove the two differences involving that element and add the difference between its neighbors.
3. Track the maximum reduction in total time.
4. Subtract the maximum reduction from the original total to obtain the answer.

## Python Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    total = sum(abs(a[i] - a[i - 1]) for i in range(1, n))
    max_reduction = 0

    for i in range(n):
        if i == 0:
            reduction = abs(a[1] - a[0])
        elif i == n - 1:
            reduction = abs(a[n - 1] - a[n - 2])
        else:
            reduction = (
                abs(a[i] - a[i - 1])
                + abs(a[i + 1] - a[i])
                - abs(a[i + 1] - a[i - 1])
            )

        max_reduction = max(max_reduction, reduction)

    print(total - max_reduction)
```

## Example

**Input

```text
3
5
4 15 1 7 9
3
2 4 8
6
11 13 17 19 23 29
```

**Output

```text
11
2
12
```

## Complexity Analysis

- **Time Complexity:** `O(n)` per test case.
- **Space Complexity:** `O(n)` for storing the array.

## Key Takeaways

- Use absolute differences to calculate movement costs.
- Optimize the total by identifying the best element to remove.
- Avoid recalculating the entire sum for every possible removal.
- Apply greedy reasoning to achieve a linear-time solution.

## Tags

`Codeforces` `Greedy` `Arrays` `Optimization` `Python` `Competitive Programming`
