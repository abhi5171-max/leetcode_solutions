This is the classic Codeforces problem 4A - Watermelon.

Key Observation

To divide the watermelon into two positive even parts:

w must be even.
w must be greater than 2.

Why?

If w is odd → odd cannot be split into two even numbers.
If w = 2 → the only split is 1 + 1, and 1 is not even.
Any even number greater than 2 can be written as:
2 + (w - 2)
Both parts are positive and even.

Examples:

8 = 2 + 6 → YES
4 = 2 + 2 → YES
2 = 1 + 1 → NO
7 → NO
Python Solution
w = int(input())

if w > 2 and w % 2 == 0:
    print("YES")
else:
    print("NO")
Time Complexity
O(1)
Space Complexity
O(1)