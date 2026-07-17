import math

A = int(input())
total = 0

for base in range(2, A):
    temp = A
    while temp > 0:
        total += temp % base
        temp //= base

denominator = A - 2
g = math.gcd(total, denominator)

print(f"{total // g}/{denominator // g}")