t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())

    if b >= 3 * a:
        ans = n * a
    else:
        ans = (n // 3) * b + min((n % 3) * a, b)

    print(ans)