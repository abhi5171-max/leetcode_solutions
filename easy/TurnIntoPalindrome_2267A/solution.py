
t = int(input())

for _ in range(t):
    n, c = input().split()
    n = int(n)
    s = input().strip()

    ans = 0

    for i in range(n // 2):
        j = n - i - 1

        if s[i] == s[j]:
            continue

        if s[i] == c or s[j] == c:
            ans += 1
        else:
            ans += 2

    print(ans)
