# A. Bigrams

## Problem Summary

A **bigram** is a pair of adjacent characters in a string.

For example:

```text
hello
```

contains the following bigrams:

```text
he, el, ll, lo
```

You are given cards containing `k` different letters, where each letter has a specified number of cards. You must use every card exactly once to create a string.

Your task is to determine whether it is possible to arrange the cards so that the resulting string contains **at least two equal bigrams**.

---

## Key Observations

### Case 1: A letter appears at least 3 times

If any letter appears three or more times, we can place three identical letters together:

```text
aaa
```

The bigrams are:

```text
aa, aa
```

Since both bigrams are equal, the answer is:

```text
YES
```

---

### Case 2: At least two letters appear at least 2 times

For example, suppose we have:

```text
aabb
```

We can arrange them as:

```text
abab
```

The bigrams are:

```text
ab, ba, ab
```

The bigram `ab` appears twice.

Therefore, if at least two letters have a frequency greater than or equal to `2`, the answer is:

```text
YES
```

---

### Otherwise

If neither of the above conditions is satisfied, it is impossible to create two equal bigrams.

For example:

```text
aab
```

Possible arrangements are:

```text
aab
aba
baa
```

None of them contain two equal bigrams.

Therefore, the answer is:

```text
NO
```

---

## Algorithm

For each test case:

1. Find the maximum frequency of any letter.
2. Count how many letters have frequency greater than or equal to `2`.
3. If:

   * Any frequency is at least `3`, or
   * At least two letters have frequency at least `2`

   Print `YES`.
4. Otherwise, print `NO`.

---

## Python 3 Solution

```python
t = int(input())

for _ in range(t):
    k = int(input())
    c = list(map(int, input().split()))

    if max(c) >= 3:
        print("YES")
    elif sum(x >= 2 for x in c) >= 2:
        print("YES")
    else:
        print("NO")
```

---

## Complexity Analysis

* **Time Complexity:** `O(k)` per test case
* **Space Complexity:** `O(k)`

Where `k ≤ 10`.

---

## Example

### Input

```text
7
1
1
1
3
1
4
2
2 1
2
3 2
3
1 1 2
4
1 1 2 2
```

### Output

```text
NO
YES
YES
NO
YES
NO
YES
```
