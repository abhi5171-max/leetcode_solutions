
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    prev_time = 0
    prev_side = 0
    ans = 0

    for _ in range(n):
        a, b = map(int, input().split())

        duration = a - prev_time
        required_moves = abs(b - prev_side)

        if (duration - required_moves) % 2 == 0:
            ans += duration
        else:
            ans += duration - 1

        prev_time = a
        prev_side = b

    ans += m - prev_time

    print(ans)
