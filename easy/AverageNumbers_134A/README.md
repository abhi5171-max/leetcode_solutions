# A. Average Numbers

## Problem Statement

You are given a sequence of `n` positive integers.

For every index `i`, determine whether the `i`-th element is equal to the **arithmetic mean of all the other elements**.

The arithmetic mean of all elements except `a[i]` is:

```text
(sum - a[i]) / (n - 1)
```

where `sum` is the sum of all elements.

Print all indices satisfying this condition.

---

## Approach

Let the total sum of the array be:

```text
S = a₁ + a₂ + ... + aₙ
```

For an element `a[i]` to be the average of all other elements:

```text
a[i] = (S - a[i]) / (n - 1)
```

Multiply both sides by `(n - 1)`:

```text
a[i] × (n - 1) = S - a[i]
```

Rearranging:

```text
a[i] × n = S
```

Therefore, an element is a valid answer **if and only if**:

```text
a[i] * n == total_sum
```

This allows us to check every element in constant time after calculating the total sum.

---

## Algorithm

1. Read `n` and the array.
2. Calculate the total sum of all elements.
3. Traverse the array.
4. For each index `i`:

   * Check whether `a[i] * n == total_sum`.
   * If true, store `i + 1` because indices are 1-based.
5. Print the number of valid indices.
6. Print the indices.

---

## Python 3 Solution

```python
n = int(input())
a = list(map(int, input().split()))

total = sum(a)
ans = []

for i in range(n):
    if a[i] * n == total:
        ans.append(i + 1)

print(len(ans))

if ans:
    print(*ans)
```

---

## Example 1

### Input

```text
5
1 2 3 4 5
```

The total sum is:

```text
15
```

For `a[3] = 3`:

```text
3 × 5 = 15
```

So it satisfies the condition.

Indeed, the average of the remaining elements is:

```text
(1 + 2 + 4 + 5) / 4 = 12 / 4 = 3
```

Therefore, index `3` is the answer.

### Output

```text
1
3
```

---

## Example 2

### Input

```text
4
50 50 50 50
```

Total sum:

```text
200
```

For every element:

```text
50 × 4 = 200
```

Therefore, every element is equal to the average of the other elements.

### Output

```text
4
1 2 3 4
```

---

## Why This Works

Suppose `a[i]` is the required element.

It must satisfy:

```text
a[i] = (total_sum - a[i]) / (n - 1)
```

Multiplying by `(n - 1)`:

```text
a[i](n - 1) = total_sum - a[i]
```

Adding `a[i]` to both sides:

```text
a[i]n = total_sum
```

Thus, checking:

```text
a[i] * n == total_sum
```

is mathematically equivalent to checking whether `a[i]` equals the average of all other elements.

---

## Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)` for storing the answer indices.

The algorithm easily handles `n ≤ 2 × 10⁵`.

---

## Key Takeaway

Instead of calculating the average separately for every element, transform the equation:

```text
a[i] = (sum - a[i]) / (n - 1)
```

into the simpler condition:

```text
a[i] * n == sum
```

This avoids floating-point calculations and gives an efficient `O(n)` solution.
