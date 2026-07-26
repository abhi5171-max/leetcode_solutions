n, m = map(int, input().split())

containers = []

for _ in range(m):
    a, b = map(int, input().split())
    containers.append((b, a))  # (matches per box, number of boxes)

containers.sort(reverse=True)

total_matches = 0
remaining = n

for matches_per_box, boxes in containers:
    if remaining == 0:
        break

    take = min(remaining, boxes)
    total_matches += take * matches_per_box
    remaining -= take

print(total_matches)