README – Function f(n)
Problem

For a positive integer n, define the function:

[
f(n) = -1 + 2 - 3 + 4 - 5 + \cdots + (-1)^n \cdot n
]

Given n, compute the value of f(n).

Approach

Instead of simulating the entire series, observe the pattern:

If n is even:
Every pair contributes 1.

Example:

-1 + 2 = 1
-3 + 4 = 1

Therefore:

f(n) = n / 2
If n is odd:
The last negative term remains unpaired.

Therefore:

f(n) = -(n + 1) / 2

This allows us to compute the answer in constant time.

Algorithm
Read the integer n.
If n is even, print n // 2.
Otherwise, print -(n + 1) // 2.
Complexity
Time Complexity: O(1)
Space Complexity: O(1)
Python Solution
n = int(input())

if n % 2 == 0:
    print(n // 2)
else:
    print(-(n + 1) // 2)