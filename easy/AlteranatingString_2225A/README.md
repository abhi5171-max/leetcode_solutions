# Codeforces — B. Alternating String

## Problem

You are given a string `s` consisting only of `'a'` and `'b'`.

In at most one operation, you can:

1. Choose a non-empty substring.
2. Optionally invert all characters in it (`a ↔ b`).
3. Reverse the chosen substring. Reversal is mandatory.

The goal is to determine whether it is possible to obtain an **alternating string**, where every two adjacent characters are different.

---

## Key Observation

Consider an adjacent pair of characters.

An **alternating string** has:

$$
n-1
$$

different adjacent pairs.

Call an adjacent pair **bad** if:

```text
s[i] == s[i+1]
```

For example:

```text
a b b a b b
    ↑     ↑
   bad   bad
```

### What happens during the operation?

When we reverse a substring, the relationships **inside the substring** are preserved, only their order is reversed.

If we invert the substring, both characters of every internal pair are changed:

```text
aa → bb
ab → ba
```

So whether the two characters are equal or different does not change.

Therefore, the only adjacent pairs whose status can change are the **two boundaries** of the selected substring.

Hence, one operation can fix at most **two bad adjacent pairs**.

Therefore:

* If the string has **0, 1, or 2 bad adjacent pairs** → `YES`
* If it has **more than 2** → `NO`

---

## Algorithm

For each test case:

1. Initialize `bad = 0`.
2. Traverse the string.
3. For every adjacent pair:

   * If `s[i] == s[i+1]`, increment `bad`.
4. If `bad <= 2`, print `YES`.
5. Otherwise, print `NO`.

---

## Complexity

For each string of length `n`:

* **Time:** `O(n)`
* **Space:** `O(1)`

Since the total length of all strings is at most `2 × 10^5`, this easily fits within the limits.

---

## Python Solution

```python
import sys


def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        s = input().strip()

        bad = 0

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                bad += 1

        if bad <= 2:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()
```

---

## Example

### Input

```text
8
abbaba
aaaaa
bababba
ab
abbaabba
bbb
ababa
aabb
```

### Output

```text
YES
NO
YES
YES
NO
YES
YES
YES
```

---

## Example Explanation

For:

```text
abbaba
```

There are two bad pairs:

```text
a b b a b a
  ↑
```

Actually, the substring `bbab` can be reversed to obtain an alternating string.

For:

```text
aaaaa
```

There are four bad adjacent pairs. One operation can affect only two boundaries, so it is impossible.

Thus:

```text
aaaaa → NO
```

For:

```text
ab
```

The string is already alternating, so:

```text
ab → YES
```

---

## Key Takeaway

The main trick is to **count adjacent equal pairs**.

```text
bad pairs <= 2  → YES
bad pairs > 2   → NO
```

This avoids simulating the possible substring operations entirely.
