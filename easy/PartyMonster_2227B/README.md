# Codeforces — B. Party Monster

## Problem

You are given a string `s` of length `n` consisting only of `(` and `)`.

You may perform the following operation **at most once**:

1. Choose any substring.
2. Remove it from the string.
3. Reinsert its characters one by one at arbitrary positions.

Determine whether it is possible to obtain a **Regular Bracket Sequence (RBS)**.

---

## Key Observation

The important trick is that we can choose **the entire string** as the substring.

After removing the entire string, we can reinsert all characters in any order.

Therefore, if the string contains an equal number of:

* `(` opening brackets
* `)` closing brackets

we can rearrange them into:

```text
()()()...
```

which is always a valid Regular Bracket Sequence.

So the answer is simply:

```text
count('(') == count(')')
```

---

## Examples

### Example 1

```text
s = "()"
```

There is already a valid bracket sequence.

```text
YES
```

### Example 2

```text
s = ")("
```

Both brackets can be rearranged:

```text
)(
↓
()
```

Therefore:

```text
YES
```

### Example 3

```text
s = "((("
```

There are 3 opening brackets and 0 closing brackets.

It is impossible to form a balanced sequence.

```text
NO
```

---

## Algorithm

For each test case:

1. Count the number of `(` characters.
2. Count the number of `)` characters.
3. If both counts are equal, print `YES`.
4. Otherwise, print `NO`.

---

## Complexity

For a string of length `n`:

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

The total length of all test cases is at most `2 × 10⁵`.

---

## Python Implementation

```python
import sys

def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        s = input().strip()

        if s.count('(') == s.count(')'):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()
```

---

## Conclusion

The seemingly complicated substring-removal and reinsertion operation has a simple solution.

Since we can select the **entire string** and rearrange all its characters arbitrarily, the only requirement is that the number of opening and closing brackets must be equal.

**Condition:**

```text
count('(') == count(')')
```

If true → `YES`
Otherwise → `NO`
