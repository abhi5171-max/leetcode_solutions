t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    ans = 0

    for i in range(n):
        if s[i] != s[-1]:
            ans += 1

    print(ans)