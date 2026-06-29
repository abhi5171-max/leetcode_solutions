import math

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

n, m = map(int, input().split())

next_prime = n + 1
while not is_prime(next_prime):
    next_prime += 1

print("YES" if next_prime == m else "NO")