# A. Carpeting the Room — README

## Problem

Soroush has a square room with side length `n`.

He has `k` square carpets, each with side length `a`. The carpets:

* Can overlap each other.
* Cannot be rotated.
* Must completely cover the room.

Determine whether it is possible to carpet the entire room.

> **Note:** The problem statement appears to have formatting corruption where the carpet side length is shown as `n1`. We use `a` for that value.

---

## Approach

To cover a room of side `n` using carpets of side `a`, we need enough carpets to cover the room along **both dimensions**.

The number of carpets needed along one dimension is:

```text
ceil(n / a)
```

Therefore, the total number of carpets required is:

```text
ceil(n / a) × ceil(n / a)
```

If `k` is at least this number, the room can be completely covered.

### Avoiding Floating Point

We can calculate:

```python
ceil(n / a) = (n + a - 1) // a
```

So:

```python
needed = ((n + a - 1) // a) ** 2
```

Then:

* `needed <= k` → `YES`
* Otherwise → `NO`

---

## Python 3 Solution

```python
n, k, a = map(int, input().split())

needed_per_side = (n + a - 1) // a
needed = needed_per_side * needed_per_side

if needed <= k:
    print("YES")
else:
    print("NO")
```

---

## Example 1

### Input

```text
10 4 6
```

Each carpet has side `6`.

Carpets needed along one side:

```text
ceil(10 / 6) = 2
```

Total carpets needed:

```text
2 × 2 = 4
```

We have `4` carpets, so:

```text
YES
```

### Output

```text
YES
```

---

## Example 2

### Input

```text
10 2 5
```

Carpets needed along one side:

```text
ceil(10 / 5) = 2
```

Total required:

```text
2 × 2 = 4
```

But only `2` carpets are available.

Therefore:

```text
NO
```

### Output

```text
NO
```

---

## Complexity

* **Time:** `O(1)`
* **Space:** `O(1)`

---

## Key Idea

The important formula is:

```text
required = ceil(n / a)²
```

If:

```text
required <= k
```

then the room can be completely covered.

---

## Topics

* Math
* Ceiling Division
* Geometry
* Implementation

**Codeforces:** A. Carpeting the Room
