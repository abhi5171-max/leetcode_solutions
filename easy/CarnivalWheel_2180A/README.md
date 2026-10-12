<!-- A. Carnival Wheel — Python Solution
Approach: Brute Force + Modulo
The pointer's position after \(k\) spins is:
\[
\text{position}=(a+k\cdot b)\bmod l
\]

Since there are only \(l\) sections and \(l\leq 5000\), we can simulate the spins and track the maximum position.
Python Code
t = int(input())for _ in range(t):    l, a, b = map(int, input().split())    pos = a    ans = a    for _ in range(l):        pos = (pos + b) % l        ans = max(ans, pos)    print(ans)

Example walkthrough
Input:
4
5 3 2
2 0 6
8 2 4
100 0 1

Output:
4
0
6
99
For the first test case, \(l=5,\ a=3,\ b=2\):
Spins	Position
0	3
1	0
2	2
3	4
4	1
5	3
The positions repeat after five spins, so the maximum prize is 4.
Complexity analysis
- Time complexity: \(O(l)\) per test case.
- Space complexity: \(O(1)\).
Key concept: The modulo operator % ensures the pointer stays within the range \(0\) to \(l-1\). Since the wheel has at most \(l\) distinct positions, simulating \(l\) spins is sufficient to find the maximum prize. -->