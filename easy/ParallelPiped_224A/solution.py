import math

x, y, z = map(int, input().split())

a = math.isqrt(x * z // y)
b = math.isqrt(x * y // z)
c = math.isqrt(y * z // x)

print(4 * (a + b + c))