import sys

def is_prime(x):
    if x < 2:
        return False

    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1

    return True


input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    print("YES" if is_prime(n + 1) else "NO")