A. Insomnia cure — Codeforces
Problem Statement

The princess counted d dragons. Every:

k-th dragon gets punched.
l-th dragon gets its tail shut.
m-th dragon gets its paws trampled.
n-th dragon is threatened.

A dragon is considered damaged if it is affected by at least one of these actions.

Find the total number of damaged dragons.

Approach

We can simply check every dragon from 1 to d.

For each dragon, if its number is divisible by any of k, l, m, or n, then it is damaged.

The condition is:

dragon % k == 0 or
dragon % l == 0 or
dragon % m == 0 or
dragon % n == 0

If the condition is true, increase the answer.

Python 3 Solution
k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

damaged = 0

for dragon in range(1, d + 1):
    if dragon % k == 0 or dragon % l == 0 or dragon % m == 0 or dragon % n == 0:
        damaged += 1

print(damaged)
Example
Input
2
3
4
5
24

The dragons that escape are:

1, 7, 11, 13, 17, 19, 23

There are 7 unharmed dragons.

Therefore:

24 - 7 = 17
Output
17
Complexity Analysis
Time Complexity: O(d)
Space Complexity: O(1)

Since d ≤ 100000, this approach easily fits within the limits.

Key Concept

Use the modulo operator % to determine whether a dragon is a multiple of a given number.

For example:

12 % 3 == 0

means dragon 12 is every 3rd dragon and therefore gets damaged.