t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()

    sleep = 0
    awake_until = -1

    for i in range(n):
        if s[i] == '1':
            awake_until = i + k
        elif i > awake_until:
            sleep += 1

    print(sleep)