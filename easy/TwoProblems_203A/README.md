Here’s a clean **README.md** with the Python 3 solution:

# Codeforces — A. Two Problems

## Problem Description

Valera participated in a Codeforces contest containing exactly **two problems**.

* The first problem initially costs `a` points and loses `da` points every minute.
* The second problem initially costs `b` points and loses `db` points every minute.
* The contest lasts for `t` minutes.
* A problem can be solved at most once.
* Valera can submit a solution at any minute from `0` to `t - 1`.

Given Valera's total score `x`, determine whether it is possible for him to obtain **exactly `x` points**.

---

## Approach

Since there are only two problems, we can generate every score that each problem can provide.

For the first problem, at minute `i`:

```text
a - i × da
```

For the second problem, at minute `j`:

```text
b - j × db
```

Valera can:

1. Solve neither problem → `0` points.
2. Solve only the first problem.
3. Solve only the second problem.
4. Solve both problems.

We check all possible combinations of submission times for the two problems.

If any combination produces exactly `x` points, the answer is `YES`. Otherwise, it is `NO`.

---

## Python 3 Solution

```python
x, t, a, b, da, db = map(int, input().split())

# Solve neither problem
if x == 0:
    print("YES")
    exit()

# Possible scores from the first problem
scores_a = [a - i * da for i in range(t)]

# Possible scores from the second problem
scores_b = [b - i * db for i in range(t)]

# Solve only the first problem
if x in scores_a:
    print("YES")
    exit()

# Solve only the second problem
if x in scores_b:
    print("YES")
    exit()

# Solve both problems
for score_a in scores_a:
    for score_b in scores_b:
        if score_a + score_b == x:
            print("YES")
            exit()

print("NO")
```

---

## Example 1

### Input

```text
30 5 20 20 3 5
```

### Explanation

Valera can solve:

* First problem at minute `0` → `20` points
* Second problem at minute `2` → `20 - 2 × 5 = 10` points

Total:

```text
20 + 10 = 30
```

Therefore, the answer is:

### Output

```text
YES
```

---

## Example 2

### Input

```text
10 4 100 5 5 1
```

No possible combination of the two problems gives exactly `10` points.

### Output

```text
NO
```

---

## Complexity Analysis

There are at most `t` possible scores for each problem.

Checking all pairs takes:

```text
Time:  O(t²)
Space: O(t)
```

Since `t ≤ 300`, this is easily fast enough.

---

## Key Takeaway

The important observation is that **each problem can be submitted only once**, so we only need to consider its possible score at each minute. With just two problems and a small constraint on `t`, brute-force enumeration is simple and reliable.
