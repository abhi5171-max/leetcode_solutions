t = int(input())

for _ in range(t):
    s = input().strip()
    best = ""

    for i in range(len(s)):
        if s[i] == '0':
            # Alice deletes this 0
            remaining = s[:i] + s[i + 1:]

            # Bob deletes the first 1
            j = remaining.index('1')
            final_string = remaining[:j] + remaining[j + 1:]

            # Alice chooses the lexicographically largest result
            best = max(best, final_string)

    print(best)