t = int(input())

for _ in range(t):
    k, x = map(int, input().split())

    for _ in range(k):
        if x > 1 and (x - 1) % 3 == 0 and ((x - 1) // 3) % 2 == 1:
            x = (x - 1) // 3
        else:
            x *= 2

    print(x)