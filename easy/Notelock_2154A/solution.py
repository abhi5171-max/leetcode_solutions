t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()

    ans = 0
    last = -k

    for i in range(n):
        if s[i] == '1':
            if i - last >= k:
                ans += 1
                last = i
            else:
                last = i

    print(ans)