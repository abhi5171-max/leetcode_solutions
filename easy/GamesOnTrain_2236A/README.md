# README — Games on the Train

Problem Statement

Dabir has n towers with heights h[i]. For every tower, we must choose an integer x[i] such that:

$$ 1 \le x_i \le k $$

and increase each tower exactly once.

The goal is to make all tower heights equal.

We need to find the minimum possible value of k.

Key Idea

Suppose the final height is H.

For every tower:

$$ x_i = H-h_i $$

Since every x[i] must be at least 1, the final height must satisfy:

$$ H > \max(h) $$

To minimize the maximum value of x[i], we should choose the smallest possible final height:

$$ H = \max(h)+1 $$

Therefore, the largest increment required is:

$$ k = (\max(h)+1)-\min(h) $$

So the answer is simply:

$$ \boxed{\max(h)-\min(h)+1} $$
Example

For:

h = [2, 6, 4]

Maximum height:

max(h) = 6

Minimum height:

min(h) = 2

Therefore:

k = 6 - 2 + 1
  = 5

We can choose:

x = [5, 1, 3]

giving:

[2+5, 6+1, 4+3]
= [7, 7, 7]

Hence the answer is 5.

Python Solution
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))

    answer = max(h) - min(h) + 1

    print(answer)
Complexity

For each test case:

Time: O(n)
Space: O(n)

Since n ≤ 5, this is easily within the limits.

Sample

Input

4
2
1 3
3
2 6 4
5
5 4 6 6 1
4
3 3 3 3

Output

3
5
6
1
Important Observation

The +1 is necessary because every tower must be increased by at least 1. We cannot leave the tallest tower unchanged.

For example:

[1, 3]

The final height must be at least 4, so the increments are:

[3, 1]

Thus:

k = 3
