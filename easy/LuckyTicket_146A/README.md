# Lucky Ticket

## Problem Statement

Petya considers a ticket **lucky** if:

1. The ticket number contains only the digits `4` and `7`.
2. The sum of digits in the first half of the ticket is equal to the sum of digits in the second half.

The ticket length `n` is always even. Determine whether the given ticket is lucky.

---

## Approach

We can solve the problem in two simple steps:

### 1. Check for lucky digits

Every character in the ticket must be either:

* `4`
* `7`

If any other digit appears, print `NO`.

### 2. Compare the two halves

Split the ticket into:

* First half: `ticket[:n//2]`
* Second half: `ticket[n//2:]`

Calculate the sum of digits in both halves.

* If the sums are equal → `YES`
* Otherwise → `NO`

---

## Python 3 Solution

```python
n = int(input())
ticket = input().strip()

# Check if all digits are lucky
if not all(ch in '47' for ch in ticket):
    print("NO")
else:
    half = n // 2

    first_sum = sum(int(ch) for ch in ticket[:half])
    second_sum = sum(int(ch) for ch in ticket[half:])

    if first_sum == second_sum:
        print("YES")
    else:
        print("NO")
```

---

## Example

### Input

```text
4
4774
```

### Explanation

First half:

```text
47
```

Sum:

```text
4 + 7 = 11
```

Second half:

```text
74
```

Sum:

```text
7 + 4 = 11
```

All digits are lucky digits (`4` and `7`), and both sums are equal.

### Output

```text
YES
```

---

## Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

where `n` is the length of the ticket.
