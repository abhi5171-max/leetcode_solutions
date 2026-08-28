Here’s a clean **README.md** for the solution:

# A. Hexadecimal's Theorem

## Problem

Given a Fibonacci number `n`, represent it as the sum of three Fibonacci numbers:

$$
n = a + b + c
$$

The three Fibonacci numbers do not need to be different.

If such a representation is impossible, print:

```text
I'm too stupid to solve this problem
```

### Fibonacci Sequence

The Fibonacci numbers are defined as:

```text
F0 = 0
F1 = 1
Fi = Fi-2 + Fi-1
```

So the sequence begins:

```text
0, 1, 1, 2, 3, 5, 8, 13, ...
```

---

## Approach

Since `n < 10^9`, there are only around 45 Fibonacci numbers that need to be considered.

### Steps

1. Generate all Fibonacci numbers less than or equal to `n`.

2. Iterate over every possible Fibonacci number `a`.

3. Iterate over every possible Fibonacci number `b`.

4. Calculate:

   ```text
   c = n - a - b
   ```

5. If `c` is also a Fibonacci number, output `a`, `b`, and `c`.

6. If no valid combination is found, print the required message.

Because the number of Fibonacci values is very small, checking all pairs is fast enough.

---

## Algorithm

```text
Generate Fibonacci numbers up to n

for every Fibonacci number a:
    for every Fibonacci number b:
        c = n - a - b

        if c is a Fibonacci number:
            print a, b, c
            stop

print "I'm too stupid to solve this problem"
```

---

## Python Implementation

```python
n = int(input())

# Generate Fibonacci numbers up to n
fib = [0, 1]

while fib[-1] + fib[-2] <= n:
    fib.append(fib[-1] + fib[-2])

# Try every possible pair
for a in fib:
    for b in fib:
        c = n - a - b

        if c in fib:
            print(a, b, c)
            exit()

print("I'm too stupid to solve this problem")
```

---

## Example 1

### Input

```text
3
```

### Output

```text
1 1 1
```

Explanation:

```text
1 + 1 + 1 = 3
```

All three numbers are Fibonacci numbers.

---

## Example 2

### Input

```text
13
```

### Output

```text
2 3 8
```

Explanation:

```text
2 + 3 + 8 = 13
```

All three numbers belong to the Fibonacci sequence.

---

## Complexity

Let `F` be the number of Fibonacci numbers up to `n`.

Since `n < 10^9`, `F` is approximately 45.

* **Time Complexity:** `O(F²)`
* **Space Complexity:** `O(F)`

This is easily fast enough for the given constraints.

---

## Key Takeaway

The important observation is that the number of Fibonacci numbers below `10^9` is very small. Therefore, a straightforward **brute-force search over pairs** is simple, reliable, and efficient.
