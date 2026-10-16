t = int(input())

for _ in range(t):
    s = input().strip()

    if s.count('Y') > 1:
        print("NO")
    else:
        print("YES")