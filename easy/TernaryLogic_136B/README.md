# B. Ternary Logic

## Problem
Given two decimal integers `a` and `c`, find the smallest integer `b` such that:

`a tor b = c`

The **tor** operation works by:
- Converting numbers to ternary (base-3).
- Padding with leading zeros if necessary.
- Adding corresponding digits modulo 3.
- No carry is generated between digits.

Finally, print `b` in decimal.

---

## Approach

Since:

```
(a_digit + b_digit) % 3 = c_digit
```

We can directly compute:

```
b_digit = (c_digit - a_digit) % 3
```

Algorithm:
1. Convert both numbers digit by digit using `% 3`.
2. Compute the corresponding digit of `b`.
3. Build the answer in base-3.
4. Convert back to decimal while constructing.

---

## Algorithm
1. Read `a` and `c`.
2. While either number has remaining ternary digits:
   - Extract last ternary digits.
   - Compute `(c_digit - a_digit) % 3`.
   - Add it to the answer with the correct power of 3.
3. Print the result.

---

## Complexity Analysis

- **Time Complexity:** `O(log₃(max(a, c)))`
- **Space Complexity:** `O(1)`

---

## Key Concept

The tor operation behaves like XOR in base-3, where every digit is added modulo 3 independently without carry.

---

## Python Solution

```python
a, c = map(int, input().split())

b = 0
place = 1

while a > 0 or c > 0:
    da = a % 3
    dc = c % 3

    db = (dc - da) % 3
    b += db * place

    a //= 3
    c //= 3
    place *= 3

print(b)
```