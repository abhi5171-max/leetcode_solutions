# B. Borze

## Problem
The Borze alphabet represents ternary digits using the following encoding:

| Borze Code | Digit |
|------------|-------|
| `.` | `0` |
| `-.` | `1` |
| `--` | `2` |

Given a valid Borze code, decode it into its corresponding ternary number.

## Approach
- Traverse the string from left to right.
- If the current character is `.`, append `0`.
- If the next two characters are `-.`, append `1`.
- Otherwise, the next two characters must be `--`, so append `2`.
- Continue until the entire string is processed.

## Algorithm
1. Read the Borze string.
2. Initialize an empty result.
3. Iterate through the string:
   - `.` → append `0`
   - `-.` → append `1`
   - `--` → append `2`
4. Print the decoded ternary number.

## Complexity Analysis
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

## Python Solution
```python
s = input()

i = 0
result = []

while i < len(s):
    if s[i] == '.':
        result.append('0')
        i += 1
    elif s[i:i+2] == '-.':
        result.append('1')
        i += 2
    else:
        result.append('2')
        i += 2

print("".join(result))
```

## Example

### Input
```
.-.--
```

### Output
```
012
```

## Key Concepts
- String Traversal
- Greedy Parsing
- Simulation
- Conditional Logic