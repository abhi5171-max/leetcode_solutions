
from math import isqrt

t = int(input())

for _ in range(t):
    s = input().strip()
    n = int(s)

    root = isqrt(n)

    if root * root == n:
        print(0, root)
    else:
        print(-1)
