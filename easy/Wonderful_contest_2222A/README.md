# A. A Wonderful Contest

## Problem

A contest contains `n` problems, and each problem has a full score of `100`.

The `i`-th problem is divided into `a[i]` subtasks. Each subtask is worth:

$$
\frac{100}{a_i}
$$

points.

A contestant can solve any number of subtasks from `0` to `a[i]`.

The task is to determine whether **every integer score from `0` to `100 × n`** can be achieved.

---

## Key Observation

To obtain **every integer score**, including `1`, we must be able to obtain exactly `1` point.

A subtask of problem `i` is worth:

$$
\frac{100}{a_i}
$$

For this to equal `1`:

$$
\frac{100}{a_i}=1
$$

Therefore:

$$
a_i=100
$$

So, the answer is:

* **Yes** → if at least one `a[i]` is `100`.
* **No** → otherwise.

If a problem has `100` subtasks, each subtask is worth `1` point, allowing us to construct every score from `0` to `100`. The remaining problems extend this continuous range to `100 × n`.

---

## Algorithm

For each test case:

1. Read `n`.
2. Read the array `a`.
3. Check whether `100` exists in the array.
4. If it exists, print `Yes`.
5. Otherwise, print `No`.

---

## Complexity

For each test case:

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

---

## Python Implementation

```python
import sys

def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        if 100 in a:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    solve()
```

---

## Example

### Input

```text
5
2
100 20
2
10 10
3
50 100 25
4
1 2 5 20
10
100 1 2 4 5 10 20 25 50 100
```

### Output

```text
Yes
No
Yes
No
Yes
```

---

## Conclusion

The entire problem reduces to checking whether **at least one problem has exactly 100 subtasks**.

```text
100 in a → Yes
otherwise → No
```
