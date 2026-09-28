# 🏐 Passing the Ball

## Problem

There are `n` students standing in a line. Each student passes the ball either to their left neighbor (`L`) or right neighbor (`R`).

The first student always passes right, and the last student always passes left.

The ball starts with student `1`. After repeatedly passing the ball according to the given directions, determine **how many different students receive the ball at least once**.

---

## 💡 Approach

We can simulate the movement of the ball.

* Start at student `1` (index `0`).
* Maintain a `visited` array to record students who have already received the ball.
* If the current student's direction is:

  * `R` → move to the next student.
  * `L` → move to the previous student.
* Continue until we reach a student that has already been visited.
* At that point, the ball is trapped in a cycle, so no new students can be reached.

### Example

For:

```text
RLRL
```

The movement is:

```text
1 → 2 → 1 → 2 → ...
```

Only students `1` and `2` receive the ball.

Therefore:

```text
Answer = 2
```

For:

```text
RRRRRL
```

The movement is:

```text
1 → 2 → 3 → 4 → 5 → 6 → 5 → 6 → ...
```

All 6 students receive the ball.

Therefore:

```text
Answer = 6
```

---

## 🧠 Algorithm

1. Read `n` and the string `s`.
2. Initialize `visited[n]` with `False`.
3. Set `pos = 0`.
4. While the current student has not been visited:

   * Mark the student as visited.
   * Increment the answer.
   * Move according to `s[pos]`.
5. Print the number of visited students.

---

## 💻 Python Implementation

```python
import sys

def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        s = input().strip()

        visited = [False] * n
        pos = 0
        ans = 0

        while not visited[pos]:
            visited[pos] = True
            ans += 1

            if s[pos] == 'R':
                pos += 1
            else:
                pos -= 1

        print(ans)

if __name__ == "__main__":
    solve()
```

---

## ⏱️ Complexity

For each test case:

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

Each student is visited at most once before the process enters a cycle.

---

## 🧪 Sample Input

```text
3
4
RLRL
6
RRRRRL
9
RRLRRRRRL
```

## 📤 Sample Output

```text
2
6
3
```

---

## 📌 Key Takeaway

The important observation is that the process is deterministic: every student has exactly one destination. Therefore, once a previously visited student is reached, the ball enters a cycle and **no new students can be visited**.

This makes a simple simulation with a `visited` array sufficient.
