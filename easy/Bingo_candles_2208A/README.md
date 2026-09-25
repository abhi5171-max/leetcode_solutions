# 🍬 Bingo Candies

## Problem

Alice has a magic `n × n` board where every cell contains a colored candy.

Bob can **rearrange the candies arbitrarily**. The goal is to determine whether the candies can be rearranged such that:

* No row contains `n` candies of the same color.
* No column contains `n` candies of the same color.

For each test case, print `YES` if such a rearrangement exists; otherwise, print `NO`.

---

## 💡 Approach

The actual positions of the candies do not matter — only the **frequency of each color** matters.

There are:

$$
n^2
$$

total cells.

For any color, if it appears more than:

$$
n^2-n
$$

times, then it is impossible to distribute those candies without creating at least one completely identical row or column.

Therefore:

* Let `maxFreq` be the maximum frequency of any color.
* If:

$$
maxFreq \leq n^2-n
$$

then the answer is `YES`.

* Otherwise, the answer is `NO`.

### Condition

```text
max_frequency <= n * n - n
```

---

## 🔍 Example

For `n = 3`:

```text
n² - n = 9 - 3 = 6
```

So a color can appear at most `6` times.

If a color appears `7` or more times, a valid rearrangement is impossible.

### Sample

```text
1 1 1
1 1 1
1 1 2
```

Frequency of color `1`:

```text
8
```

Since:

```text
8 > 6
```

the answer is:

```text
NO
```

---

## 🧠 Algorithm

For every test case:

1. Read `n`.
2. Count the frequency of every color.
3. Find the maximum frequency.
4. Check whether:

   ```text
   max_frequency <= n² - n
   ```

5. Print `YES` or `NO`.

---

## 💻 Python Implementation

```python
import sys

def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())

        freq = {}

        for _ in range(n):
            row = map(int, input().split())

            for color in row:
                freq[color] = freq.get(color, 0) + 1

        max_freq = max(freq.values())

        if max_freq <= n * n - n:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()
```

---

## ⏱️ Complexity

Let the board size be `n × n`.

* **Time Complexity:** `O(n²)`
* **Space Complexity:** `O(n²)` in the worst case.

The solution is efficient because the total sum of `n` over all test cases is at most `500`.

---

## 📌 Key Takeaway

> The arrangement of candies initially does not matter. Count how many times each color occurs and check whether the most frequent color exceeds `n² - n`.

**Condition to remember:**

```text
max_frequency > n² - n  → NO
max_frequency <= n² - n → YES
```
