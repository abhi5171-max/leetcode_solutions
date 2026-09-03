# B. Help Kingdom of Far Far Away 2

## Problem Statement

Convert a given number into the required **financial format**.

The financial format follows these rules:

* The integer and fractional parts are separated by `.`.
* The integer part is divided into groups of three digits using `,`.
* The fractional part must contain exactly **two digits**:

  * If it has fewer than two digits, append zeros.
  * If it has more than two digits, discard the extra digits without rounding.
* A negative number is represented using parentheses instead of `-`.
* The `$` symbol is placed immediately before the number.
* For negative numbers, `$` is placed **inside** the parentheses.

### Examples

```text
2012          → $2,012.00
0.000         → $0.00
-0.009876543  → ($0.00)
-12345678.9   → ($12,345,678.90)
```

---

## Approach

### 1. Check the sign

If the number starts with `-`, remember that it is negative and remove the minus sign.

```python
negative = s.startswith('-')
```

### 2. Separate integer and fractional parts

If `.` exists, split the number into:

```text
integer_part.fractional_part
```

Otherwise, the fractional part is empty.

For example:

```text
12345678.9
```

becomes:

```text
integer = 12345678
fraction = 9
```

### 3. Format the integer part

Insert commas from the right side in groups of three digits.

For example:

```text
12345678
```

becomes:

```text
12,345,678
```

Python's formatting makes this simple:

```python
f"{int(integer):,}"
```

### 4. Format the fractional part

Only the first two digits are required.

```python
fraction = (fraction + "00")[:2]
```

Examples:

```text
9       → 90
12      → 12
98765   → 98
```

No rounding is performed.

### 5. Construct the result

For a positive number:

```text
$12,345,678.90
```

For a negative number:

```text
($12,345,678.90)
```

Importantly, the brackets depend only on whether the **original input** had a minus sign. Even `-0.009` remains negative and is formatted as:

```text
($0.00)
```

---

## Python 3 Solution

```python
s = input().strip()

# Check whether the original number is negative
negative = s.startswith('-')

# Remove the minus sign
if negative:
    s = s[1:]

# Split integer and fractional parts
if '.' in s:
    integer_part, fraction_part = s.split('.')
else:
    integer_part = s
    fraction_part = ''

# Format integer part with commas
integer_part = f"{int(integer_part):,}"

# Keep exactly two fractional digits
fraction_part = (fraction_part + "00")[:2]

# Build the financial format
result = f"${integer_part}.{fraction_part}"

# Add parentheses for negative numbers
if negative:
    result = f"({result})"

print(result)
```

---

## Example Walkthrough

### Input

```text
-12345678.9
```

After removing `-`:

```text
12345678.9
```

Integer part:

```text
12345678 → 12,345,678
```

Fractional part:

```text
9 → 90
```

Financial representation:

```text
$12,345,678.90
```

Since the original number was negative:

```text
($12,345,678.90)
```

### Output

```text
($12,345,678.90)
```

---

## Edge Case

For:

```text
-0.00987654321
```

The fractional part is truncated:

```text
00987654321 → 00
```

The result is:

```text
($0.00)
```

We **do not** remove the parentheses because the original input was negative.

---

## Complexity

Let `n` be the length of the input.

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

The solution easily handles the maximum input length of 100 characters.

---

## Key Takeaways

* Use `f"{number:,}"` to insert commas into the integer part.
* Pad the fractional part with zeros and take exactly two digits.
* **Never round** the fractional part.
* Preserve the original sign even when the formatted value becomes `$0.00`.
* Put `$` inside the parentheses for negative values.
