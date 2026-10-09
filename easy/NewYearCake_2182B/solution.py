t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    white = dark = 0
    layers = 0
    size = 1

    while True:
        if layers % 2 == 0:
            white += size
        else:
            dark += size

        if white > a or dark > b:
            break

        layers += 1
        size *= 2

    white = dark = 0
    layers2 = 0
    size = 1

    while True:
        if layers2 % 2 == 0:
            dark += size
        else:
            white += size

        if white > a or dark > b:
            break

        layers2 += 1
        size *= 2

    print(max(layers, layers2))