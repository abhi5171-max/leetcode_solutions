import math

n, x, y = map(int, input().split())

required = math.ceil(n * y / 100)

print(max(0, required - x))