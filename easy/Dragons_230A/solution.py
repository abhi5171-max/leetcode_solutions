s, n = map(int, input().split())

dragons = []

for _ in range(n):
    x, y = map(int, input().split())
    dragons.append((x, y))

# Sort dragons by strength
dragons.sort()

for x, y in dragons:
    if s <= x:
        print("NO")
        break
    s += y
else:
    print("YES")