import math

Y, W = map(int, input().split())

mx = max(Y, W)
favorable = 7 - mx
total = 6

g = math.gcd(favorable, total)

print(f"{favorable // g}/{total // g}")