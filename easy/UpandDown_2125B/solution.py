
from math import gcd

t = int(input())

for _ in range(t):
    a, b, k = map(int, input().split())

    g = gcd(a, b)
    required = (max(a, b) + k - 1) // k

    if g >= required:
        print(1)
    else:
        print(2)
