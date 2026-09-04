# A. Shooshuns and Sequence — Python 3

## Approach

The operation always:

1. Takes the **k-th element** of the current sequence.
2. Appends it to the end.
3. Removes the first element.

The important observation is that the elements from position `k` onward determine what value gets repeatedly appended.

For all elements to eventually become equal, the value at position `k` must be equal to every element from position `k` through `n`.

So:

* Let `x = a[k-1]`.
* Check whether `a[k-1:]` contains only `x`.
* If not, it is impossible → `-1`.
* Otherwise, we need to remove all elements before position `k` that are different from `x`.

The number of such elements is the answer.

### Example

```text
n = 3, k = 2
a = [3, 1, 1]
```

Here:

```text
a[k-1:] = [1, 1]
```

All are equal to `1`.

There is one element before position `k` that differs from `1`:

```text
[3, 1, 1]
 ^
```

After one operation:

```text
[1, 1, 1]
```

Answer:

```text
1
```

### Python 3 Code

```python
n, k = map(int, input().split())
a = list(map(int, input().split()))

x = a[k - 1]

# Every element from position k to n
# must already be equal to a[k-1].
for i in range(k - 1, n):
    if a[i] != x:
        print(-1)
        break
else:
    # Count elements before position k
    # that are different from x.
    ans = 0

    for i in range(k - 1):
        if a[i] != x:
            ans += 1

    print(ans)
```

---

## README

## Problem

Given a sequence of `n` integers and an integer `k`, an operation:

* takes the `k`-th element,
* appends it to the end,
* removes the first element.

Find the minimum number of operations needed to make all elements equal.

If it is impossible, print `-1`.

---

## Key Observation

Let:

```text
x = a[k]
```

(using 1-based indexing).

The operation always copies the element currently at position `k`.

For the sequence to eventually become completely equal, all elements from the original position `k` to `n` must already be equal to `x`.

Therefore, we check:

```text
a[k], a[k+1], ..., a[n]
```

If any of them differs from `x`, the answer is:

```text
-1
```

Otherwise, the only elements that need to disappear are the elements before position `k` that are different from `x`.

Each operation removes exactly one element from the front.

Hence:

```text
answer = number of elements among a[1 ... k-1] different from x
```

---

## Complexity

We scan the array at most twice:

```text
Time Complexity:  O(n)
Space Complexity: O(1)
```

The input array itself requires `O(n)` space.

### Quick Formula

If:

```text
x = a[k-1]
```

then:

```text
if any(a[i] != x for i in range(k-1, n)):
    answer = -1
else:
    answer = count(a[i] != x for i in range(k-1))
```

This gives an efficient solution within the `n ≤ 10^5` constraint.
