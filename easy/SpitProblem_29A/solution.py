n = int(input())

camels = {}

for _ in range(n):
    x, d = map(int, input().split())
    camels[x] = d

for x, d in camels.items():
    target = x + d
    if target in camels and target + camels[target] == x:
        print("YES")
        break
else:
    print("NO")