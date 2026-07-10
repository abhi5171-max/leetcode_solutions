import math

a, b, n = map(int, input().split())

simon_turn = True

while True:
    if simon_turn:
        take = math.gcd(a, n)
    else:
        take = math.gcd(b, n)

    if n < take:
        print(1 if simon_turn else 0)
        break

    n -= take
    simon_turn = not simon_turn