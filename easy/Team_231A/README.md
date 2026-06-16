This is the classic Codeforces problem 231A - Team.

Idea

For each problem, count how many of the three friends are sure about the solution (1 means sure, 0 means not sure).

If the sum of the three numbers is at least 2, they will solve that problem.
Count how many problems satisfy this condition.
Python Solution
n = int(input())
count = 0

for _ in range(n):
    p, v, t = map(int, input().split())
    if p + v + t >= 2:
        count += 1

print(count)
Example

Input:

3
1 1 0
1 1 1
1 0 0

Sums:

1+1+0 = 2 → solve
1+1+1 = 3 → solve
1+0+0 = 1 → don't solve

Output:

2