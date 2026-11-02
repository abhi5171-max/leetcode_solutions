
t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    possible = True

    for k in range(n, 0, -1):

        positions = [i for i in range(n) if p[i] > 0]

        if len(positions) != k:
            possible = False
            break

        if positions[-1] - positions[0] + 1 != k:
            possible = False
            break

        for i in positions:
            p[i] -= 1

    print("YES" if possible else "NO")
