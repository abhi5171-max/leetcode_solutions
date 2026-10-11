t = int(input())

for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()

    ans = 0
    possible = True

    for parity in range(2):
        pos_a = [i for i in range(parity, n, 2) if a[i] == '1']
        pos_b = [i for i in range(parity, n, 2) if b[i] == '1']

        if len(pos_a) != len(pos_b):
            possible = False
            break

        for x, y in zip(pos_a, pos_b):
            ans += abs(x - y) // 2

    print(ans if possible else -1)