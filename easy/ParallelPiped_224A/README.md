## A. Parallelepiped — Python 3

### Approach

Let the three edge lengths be `a`, `b`, and `c`.

The three given face areas are:

```text
ab = x
bc = y
ac = z
```

Multiplying all three:

```text
(ab)(bc)(ac) = a²b²c²
```

Therefore:

```text
abc = √(xyz)
```

We can recover each edge:

```text
a = √(xz / y)
b = √(xy / z)
c = √(yz / x)
```

A parallelepiped has **4 edges of each length**, so the required answer is:

```text
4(a + b + c)
```

### Python 3 Solution

```python
import math

x, y, z = map(int, input().split())

a = math.isqrt(x * z // y)
b = math.isqrt(x * y // z)
c = math.isqrt(y * z // x)

print(4 * (a + b + c))
```

### Example

For:

```text
4 6 6
```

We get:

```text
a = √(4 × 6 / 6) = 2
b = √(4 × 6 / 6) = 2
c = √(6 × 6 / 4) = 3
```

Thus:

```text
4 × (2 + 2 + 3) = 28
```

### Complexity

* **Time:** `O(1)`
* **Space:** `O(1)`
