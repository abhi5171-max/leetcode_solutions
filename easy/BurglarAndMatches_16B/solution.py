n, m = map(int, input().split())

containers = []
for _ in range(m):
    a, b = map(int, input().split())
    containers.append((b, a))  # (matches per box, number of boxes)

# Take boxes with the most matches first
containers.sort(reverse=True)

total = 0

for matches_per_box, boxes in containers:
    take = min(n, boxes)
    total += take * matches_per_box
    n -= take
    if n == 0:
        break

print(total)