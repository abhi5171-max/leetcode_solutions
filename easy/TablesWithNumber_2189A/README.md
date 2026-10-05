# A. Table with Numbers — Explanation + Python Solution

## Key Idea

We need to maximize the number of **valid pairs** `(x, y)` where:

```text
1 ≤ x ≤ h
1 ≤ y ≤ l
```

Each valid pair contributes `1` to the table.

So we need to choose as many array elements as possible and pair them such that:

- one number is a valid **row** (`≤ h`)
- the other is a valid **column** (`≤ l`)

There are two important groups:

- `both` = numbers `≤ min(h, l)` → can be used as either row or column.
- `rowOnly` = numbers `≤ h` but `> l` → can only be rows.
- `colOnly` = numbers `≤ l` but `> h` → can only be columns.

The maximum number of pairs is:

```text
min(
    number of usable elements // 2,
    number of possible row-column matches
)
```

A simpler way is to count:

```python
rows = number of a[i] <= h
cols = number of a[i] <= l
both = number of a[i] <= min(h, l)
```

The answer is:

```text
min(rows, cols, n // 2)
```

### Why?

Every pair needs:

- one element that can represent a row
- one element that can represent a column

So we cannot create more than:

- `rows` pairs because each pair needs a row,
- `cols` pairs because each pair needs a column,
- `n // 2` pairs because every pair uses two elements.

Therefore:

\[
\boxed{\text{answer}=\min(rows,cols,\lfloor n/2\rfloor)}
\]

---

## Python Solution

```python
t = int(input())

for _ in range(t):
    n, h, l = map(int, input().split())
    a = list(map(int, input().split()))

    rows = 0
    cols = 0

    for x in a:
        if x <= h:
            rows += 1

        if x <= l:
            cols += 1

    answer = min(rows, cols, n // 2)

    print(answer)
```

### Example

For:

```text
n = 5, h = 2, l = 2
a = [1, 2, 2, 3, 2]
```

Numbers that can be rows:

```text
1, 2, 2, 2 → rows = 4
```

Numbers that can be columns:

```text
1, 2, 2, 2 → cols = 4
```

Maximum number of pairs due to available elements:

```text
n // 2 = 2
```

Therefore:

```text
answer = min(4, 4, 2)
       = 2
```

Output:

```text
2
```

### Complexity

- **Time:** `O(n)` per test case
- **Space:** `O(n)` for storing the array

Since the total `n ≤ 100 × 500 = 50,000`, this is easily within the limits.
