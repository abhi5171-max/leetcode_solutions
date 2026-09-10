t = int(input())

for _ in range(t):
    k = int(input())
    c = list(map(int, input().split()))

    if max(c) >= 3:
        print("YES")
    elif sum(x >= 2 for x in c) >= 2:
        print("YES")
    else:
        print("NO")