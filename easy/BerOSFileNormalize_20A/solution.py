s = input().strip()
ans = []
i = 0

while i < len(s):
    if s[i] == '/':
        ans.append('/')
        while i + 1 < len(s) and s[i + 1] == '/':
            i += 1
    else:
        ans.append(s[i])
    i += 1

result = "".join(ans)

if len(result) > 1 and result[-1] == '/':
    result = result[:-1]

print(result)