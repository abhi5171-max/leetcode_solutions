s = input().strip()
n = len(s)

ans = 0

for length in range(1, n):
    seen = set()
    for i in range(n - length + 1):
        sub = s[i:i + length]
        if sub in seen:
            ans = max(ans, length)
            break
        seen.add(sub)

print(ans)