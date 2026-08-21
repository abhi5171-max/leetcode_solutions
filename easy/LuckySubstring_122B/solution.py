
s = input().strip()

freq = {}

n = len(s)

for i in range(n):
    for j in range(i + 1, n + 1):
        sub = s[i:j]

        # A lucky substring contains only 4 and 7
        if all(c in "47" for c in sub):
            freq[sub] = freq.get(sub, 0) + 1

if not freq:
    print(-1)
else:
    # Maximum frequency first,
    # lexicographically smallest in case of a tie
    answer = min(freq, key=lambda x: (-freq[x], x))
    print(answer)