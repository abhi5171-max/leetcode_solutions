## A. Postcards and Photos — README

### Problem

We have a row of objects consisting of:

* `C` — postcard
* `P` — photo

Polycarpus removes objects **from left to right** and cannot skip any object.

He has two restrictions:

1. He cannot carry postcards and photos at the same time.
2. He can carry at most **5 objects**.

Whenever his hands are full or the type of object changes, he may need to visit the closet.

The goal is to find the **minimum number of closet visits** required to remove all objects.

### Approach

Process the string from left to right.

For every **consecutive group of the same type**:

* Count how many objects are in that group.
* Since Polycarpus can carry at most 5 objects, the number of visits required is:

```text
ceil(group_size / 5)
```

For example:

```text
CCCCCC
```

has 6 postcards:

```text
6 / 5 → 2 visits
```

Similarly:

```text
CCCCCCCCCC
```

has 10 postcards:

```text
10 / 5 → 2 visits
```

We can calculate the ceiling without floating-point arithmetic:

```python
(group_size + 4) // 5
```

### Example

For:

```text
CCCCCCPPCPPPPPPPPPP
```

The consecutive groups are:

```text
CCCCCC      → 6 C → 2 visits
PP          → 2 P → 1 visit
C           → 1 C → 1 visit
PPPPPPPPPP  → 10 P → 2 visits
```

Total:

```text
2 + 1 + 1 + 2 = 6
```

### Complexity

* **Time:** `O(n)`
* **Space:** `O(1)`

### Python 3 Solution

We can also process each group using a simple loop:

```python
s = input().strip()

ans = 0
i = 0

while i < len(s):
    j = i

    while j < len(s) and s[j] == s[i]:
        j += 1

    length = j - i
    ans += (length + 4) // 5

    i = j

print(ans)
```

