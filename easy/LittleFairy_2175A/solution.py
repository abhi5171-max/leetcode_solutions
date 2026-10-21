t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    colors = set(a)
    k = len(colors)

    while k not in colors:
        colors.add(k)
        k = len(colors)

    print(k)