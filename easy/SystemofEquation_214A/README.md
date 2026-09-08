# 🧮 A. System of Equations

## 📌 Problem

You are given two integers `n` and `m` and the following system of equations:

$$
a^2 + b = n
$$

$$
a + b^2 = m
$$

The task is to count the number of pairs of non-negative integers `(a, b)` that satisfy both equations.

---

## 💡 Approach

From the first equation:

$$
b = n - a^2
$$

We can iterate through all possible values of `a`.

For each `a`:

1. Calculate `b = n - a²`.
2. Check whether `b` is non-negative.
3. Verify the second equation:

$$
a + b^2 = m
$$

4.If both equations are satisfied, increment the answer.

---

## 💻 Solution

```python
n, m = map(int, input().split())

count = 0

for a in range(1001):
    b = n - a * a

    if b >= 0 and a + b * b == m:
        count += 1

print(count)
```

---

## ⏱️ Complexity Analysis

| Complexity       | Value |
| ---------------- | ----- |
| Time Complexity  | O(√n) |
| Space Complexity | O(1)  |

---

## 📝 Example

### Input

```text
9 3
```

### Valid Pair

```text
a = 3
b = 0
```

Verification:

$$
3^2 + 0 = 9
$$

$$
3 + 0^2 = 3
$$

### Output

```text
1
