# 📦 Towers of Boxes

## Problem

Monocarp has `n` identical boxes. Each box has:

* Weight = `w`
* Durability = `d`

He wants to arrange all boxes into the **minimum possible number of towers**.

A box is safe if the total weight of all boxes placed above it does not exceed its durability.

The task is to determine the minimum number of towers required.

---

## 💡 Key Observation

Consider a tower containing `k` boxes.

The bottom box has `k - 1` boxes above it, so the total weight above it is:

$$
(k-1)w
$$

For the tower to be safe:

$$
(k-1)w \le d
$$

Therefore:

$$
k-1 \le \frac{d}{w}
$$

The maximum number of boxes that can be placed in one tower is:

$$
\boxed{k = \left\lfloor\frac{d}{w}\right\rfloor + 1}
$$

Once we know the maximum tower size, we simply divide `n` boxes into groups of that size.

Thus, the minimum number of towers is:

$$
\boxed{\left\lceil\frac{n}{k}\right\rceil}
$$

Using integer arithmetic:

$$
\boxed{\frac{n+k-1}{k}}
$$

---

## 🧠 Algorithm

For every test case:

1. Read `n`, `w`, and `d`.
2. Calculate the maximum number of boxes per tower:

   ```text
   max_boxes = d / w + 1
   ```

   using integer division.
3. Calculate the minimum number of towers:

   ```text
   towers = (n + max_boxes - 1) / max_boxes
   ```

4. Print the answer.

---

## 💻 Python Implementation

```python
import sys

def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n, w, d = map(int, input().split())

        max_boxes = d // w + 1

        towers = (n + max_boxes - 1) // max_boxes

        print(towers)

if __name__ == "__main__":
    solve()
```

---

## 🔎 Example

### Input

```text
3
8 10 20
8 1 20
5 3 2
```

### Case 1

```text
n = 8
w = 10
d = 20
```

Maximum boxes in one tower:

$$
\left\lfloor\frac{20}{10}\right\rfloor + 1 = 3
$$

Therefore:

$$
\left\lceil\frac{8}{3}\right\rceil = 3
$$

Answer:

```text
3
```

### Case 2

```text
n = 8
w = 1
d = 20
```

Maximum boxes:

$$
\left\lfloor\frac{20}{1}\right\rfloor+1=21
$$

Since there are only 8 boxes, all can be placed in one tower.

Answer:

```text
1
```

### Case 3

```text
n = 5
w = 3
d = 2
```

Since one box weighs more than the durability:

$$
\left\lfloor\frac{2}{3}\right\rfloor+1=1
$$

Only one box can be placed in each tower.

Answer:

```text
5
```

---

## 📤 Sample Output

```text
3
1
5
```

---

## ⏱️ Complexity

For each test case:

* **Time Complexity:** `O(1)`
* **Space Complexity:** `O(1)`

The solution uses only a few arithmetic operations, making it efficient even for a large number of test cases.

---

## 📌 Key Takeaway

The entire problem reduces to finding the **maximum safe tower height**:

$$
\boxed{\text{max\_boxes} = \frac{d}{w}+1}
$$

Then:

$$
\boxed{\text{towers} = \left\lceil\frac{n}{\text{max\_boxes}}\right\rceil}
$$

So no simulation or sorting is required.
