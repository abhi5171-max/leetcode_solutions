
# A. Vasya and the Bus

## Problem Description

Vasya wants to find the minimum and maximum possible total bus fare paid by `n` grown-ups and `m` children.

### Fare Rules

* Each grown-up pays `1` ruble for their ticket.
* At most one child can ride for free with each grown-up.
* All other children must pay `1` ruble.
* Children cannot ride without at least one grown-up.

If the given number of grown-ups and children cannot travel according to these rules, print `Impossible`.

---

## Approach

### Impossible Case

If there are children but no grown-ups:

```text
n = 0 and m > 0
```

Children cannot travel alone, so the answer is:

```text
Impossible
```

---

## Minimum Fare

To minimize the total fare, we want to maximize the number of children traveling for free.

Each grown-up can allow at most one child to travel for free.

Therefore, at most `n` children can travel for free.

The number of children who need to pay is:

```text
max(0, m - n)
```

Since all `n` grown-ups pay, the minimum fare is:

```text
minimum = n + max(0, m - n)
```

---

## Maximum Fare

To maximize the total fare, we want to minimize the number of children traveling for free.

All children can ride with one grown-up, so only one child needs to travel for free.

The remaining children pay.

Therefore:

```text
maximum = n + max(0, m - 1)
```

---

## Python 3 Solution

```python
n, m = map(int, input().split())

if n == 0 and m > 0:
    print("Impossible")
else:
    minimum = n + max(0, m - n)
    maximum = n + max(0, m - 1)

    print(minimum, maximum)
```

---

## Example

### Input

```text
2 2
```

### Minim Fare

Each grown-up takes one child for free:

```text
2 rubles
```

### Maxim Fare

One grown-up rides with both children:

* Grown-up ticket = `1`
* One child = free
* One child = `1`

The other grown-up pays `1`.

```text
3 rubles
```

### Output

```text
2 3
```

---

## Complexity Analysis

* **Time Complexity:** `O(1)`
* **Space Complexity:** `O(1)`

---

## Key Takeaway

To find the minimum fare, maximize the number of free children. To find the maximum fare, minimize the number of free children while ensuring every child travels with at least one grown-up.
