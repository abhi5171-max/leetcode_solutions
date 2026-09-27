# Codeforces 2204B — Right Maximum

## Problem

You are given an array `a` of length `n`.

While the array is not empty:

1. Find the **maximum element** in the current array.
2. If there are multiple maximum elements, choose the **rightmost** one.
3. Remove that element and **all elements to its right**.

The task is to determine the number of operations required to make the array empty.

## Approach

The important observation is that every operation removes a suffix of the current array.

Therefore, we can process the array from **right to left**.

Maintain:

* `mx` = maximum value seen so far.
* `ans` = number of operations.

Whenever we encounter an element greater than or equal to the current maximum, it can become the maximum selected during the process.

Because the **rightmost maximum** is selected, equal maximum values are handled naturally by processing from right to left.

A simpler equivalent implementation is to maintain the maximum value while scanning from right to left and count how many times a new maximum is encountered.

## Algorithm

```text
Initialize mx = -∞
Initialize ans = 0

Traverse the array from right to left:

    if a[i] >= mx:
        mx = a[i]
        ans++

Print ans
```

## Python Implementation

```python
import sys

def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        mx = -1
        ans = 0

        for i in range(n - 1, -1, -1):
            if a[i] >= mx:
                mx = a[i]
                ans += 1

        print(ans)


if __name__ == "__main__":
    solve()
```

## Example

### Input

```text
4
5
2 1 2 3 1
6
1 2 3 4 5 6
3
3 2 1
4
1 3 3 1
```

### Output

```text
3
6
1
3
```

For the first test case:

```text
2 1 2 3 1
```

The operations are:

```text
[2, 1, 2, 3, 1]
          ↑
          3
```

After choosing `3`:

```text
[2, 1, 2]
       ↑
       2
```

After choosing `2`:

```text
[2, 1]
 ↑
 2
```

So the answer is `3`.

## Complexity

* **Time:** `O(n)` per test case
* **Space:** `O(n)` for the input array

Since the sum of `n` over all test cases is at most `2 × 10^5`, this easily fits the constraints.

## Key Takeaway

The operation always removes a suffix. Processing the array from **right to left** lets us identify the elements that can serve as the maximum of the remaining prefix.

**Pattern:** When an operation repeatedly removes a suffix based on a maximum, try looking at **right-to-left maxima**.
