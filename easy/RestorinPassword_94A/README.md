Here’s a clean **README.md** with an efficient Python 3 solution.

# Restoring Password

## Problem

Igor's password was encrypted into an 80-character binary string.

* Every **10 consecutive bits** represent one decimal digit.
* There are exactly **8 digits** in the original password.
* The next 10 input lines give the binary code corresponding to digits `0` through `9`.
* All digit codes are distinct.

The task is to decode the 80-bit encrypted password.

## Approach

1. Read the encrypted 80-bit string.
2. Store the 10-bit code for each digit from `0` to `9` in a dictionary.
3. Split the encrypted string into chunks of 10 characters.
4. For every chunk:

   * Look it up in the dictionary.
   * Append the corresponding digit to the answer.
5. Print the resulting 8-digit password.

### Complexity

* **Time:** `O(80)`
* **Space:** `O(10)`

## Python 3 Solution

```python
# Restoring Password
# Codeforces

encrypted = input().strip()

codes = {}

# Read codes for digits 0 to 9
for digit in range(10):
    code = input().strip()
    codes[code] = str(digit)

answer = []

# Each digit is represented by 10 bits
for i in range(0, 80, 10):
    chunk = encrypted[i:i + 10]
    answer.append(codes[chunk])

print("".join(answer))
```

## Example

### Input

```text
01001100100101100000010110001001011001000101100110010110100001011010100101101100
0100110000
0100110010
0101100000
0101100010
0101100100
0101100110
0101101000
0101101010
0101101100
0101101110
```

### Output

```text
12345678
```

## Key Concept

The important observation is that the encrypted password is already divided into fixed-size blocks:

```text
80 bits = 8 × 10-bit codes
```

So we simply map each 10-bit block back to its corresponding digit using a dictionary.
