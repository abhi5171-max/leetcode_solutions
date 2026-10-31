t = int(input())

for _ in range(t):
    x, y = map(int, input().split())

    if x < y:
        print(2)
    elif y >= 2 and x >= y + 2:
        print(3)
    else:
        print(-1)