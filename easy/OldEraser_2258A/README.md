# Codeforces A. Odd Eraser

## Problem Description

Given an array of integers, we can repeatedly remove elements according to the specified odd-index selection operation. The goal is to maximize the GCD of the remaining array.

## Approach

The first and last elements of the array cannot be removed by the given operation. Every valid final array must therefore contain both elements.

The maximum possible GCD is the GCD of the first and last elements:

\[
\text{Answer}=\gcd(a_1,a_n)
\]

In Python, we can calculate this using `math.gcd()`.

## Python Solution

```python
import math

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    print(math.gcd(a[0], a[-1]))
```

## Example

**Input

```text
4
7
2 4 6 7 8 9 10
2
55 55555
4
1000000 1000 1 1000000000
5
23 32 23 32 23
```

**Output

```text
2
5
1000000
23
```

## Complexity Analysis

- **Time Complexity:** \(O(n+\log A)\) per test case.
- **Space Complexity:** \(O(n)\) for storing the array.

## Topics

- Arrays
- Greatest Common Divisor (GCD)
- Number Theory
- Implementation
