# Codeforces 2267A — A. Turn Into a Palindrome

## Problem Description

Ali is given a string `s` of length `n` and a lowercase character `c`. In one operation, he can replace any character in `s` with `c`.

The task is to determine the minimum number of operations required to make the string a palindrome.

## Approach

**Concepts:** Strings, Two Pointers, Greedy Algorithm

1. Iterate through the first half of the string.
2. Compare each character `s[i]` with its mirrored character `s[n-i-1]`.
3. If both characters are equal, no operation is needed.
4. If the characters differ and one of them is already `c`, one replacement is sufficient.
5. If both characters differ from `c`, two replacements are required.
6. Add the required operations for every mirrored pair and print the total.

## Python Solution

```python
t = int(input())

for _ in range(t):
    n, c = input().split()
    n = int(n)
    s = input().strip()

    ans = 0

    for i in range(n // 2):
        j = n - i - 1

        if s[i] == s[j]:
            continue

        if s[i] == c or s[j] == c:
            ans += 1
        else:
            ans += 2

    print(ans)
```

## Example

**Input

```text
5
4 b
abca
3 p
xyx
5 e
abcbb
8 d
adbccbad
10 c
codeforces
```

**Output

```text
1
0
2
2
8
```

## Complexity Analysis

- **Time Complexity:** `O(n)` per test case.
- **Auxiliary Space Complexity:** `O(1)`, excluding the input string.

## Key Learning

- Comparing mirrored characters to identify mismatches.
- Applying greedy decisions to minimize operations.
- Handling odd and even string lengths.
- Using two pointers to process a string efficiently.
