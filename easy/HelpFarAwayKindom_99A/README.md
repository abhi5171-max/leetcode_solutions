# README — Codeforces A. Help Far Away Kingdom

## Problem Description

Given a decimal number containing an integer part and a fractional part, round it according to the following rules:

* If the last digit of the integer part is **not `9`**:

  * If the fractional part is `< 0.5`, keep the integer part.
  * If the fractional part is `>= 0.5`, increase the last digit of the integer part by `1`.
* If the integer part ends with `9`, print:

  ```text
  GOTO Vasilisa.
  ```

The input can contain up to 1000 characters.

## Approach

We only need to inspect:

1. The integer part.
2. The first digit of the fractional part.

The fractional part is at least `0.5` exactly when its **first digit is `5` or greater**.

### Cases

Suppose the input is:

```text
1.49
```

The first fractional digit is `4`, so:

```text
1.49 → 1
```

For:

```text
1.50
```

The first fractional digit is `5`, so:

```text
1.50 → 2
```

If the integer part ends in `9`, we don't perform the carry ourselves:

```text
123456789.999
```

Output:

```text
GOTO Vasilisa.
```

## Algorithm

1. Read the number as a string.
2. Split it at `.` into integer and fractional parts.
3. If the last digit of the integer part is `9`, print `GOTO Vasilisa.`
4. Otherwise, check the first fractional digit.
5. If it is less than `5`, print the integer part.
6. Otherwise, increment the last digit of the integer part.
7. Print the resulting integer.

## Python 3 Solution

```python
s = input().strip()

integer_part, fractional_part = s.split('.')

# If integer part ends with 9, carrying is not allowed
if integer_part[-1] == '9':
    print("GOTO Vasilisa.")
else:
    # Fractional part >= 0.5
    if fractional_part[0] >= '5':
        last_digit = int(integer_part[-1])
        integer_part = integer_part[:-1] + str(last_digit + 1)

    print(integer_part.lstrip('0') or '0')
```

## Example Walkthrough

### Input

```text
2.71828182845904523536
```

The integer part is:

```text
2
```

The first fractional digit is `7`, which is `>= 5`.

Therefore:

```text
2 → 3
```

Output:

```text
3
```

### Input

```text
3.14159265358979323846
```

The first fractional digit is `1`, which is `< 5`.

Therefore, the integer part remains unchanged:

```text
3
```

### Input

```text
123456789123456789.999
```

The integer part ends with `9`, so we cannot perform the carry operation.

Output:

```text
GOTO Vasilisa.
```

## Complexity

Let `n` be the length of the input.

* Splitting the string: `O(n)`
* Checking and constructing the result: `O(n)`

**Time Complexity:** `O(n)`

**Space Complexity:** `O(n)`

## Key Takeaway

The problem does **not** require floating-point arithmetic. Since only rounding at `0.5` matters, checking the **first digit after the decimal point** is sufficient. This also avoids precision problems with large numbers.
