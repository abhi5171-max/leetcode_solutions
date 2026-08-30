s = input()
t = input()

if len(s) != len(t):
    print("NO")
else:
    diff = []

    for i in range(len(s)):
        if s[i] != t[i]:
            diff.append(i)

    if len(diff) == 2:
        i, j = diff

        if s[i] == t[j] and s[j] == t[i]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")