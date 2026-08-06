sizes = ["S", "M", "L", "XL", "XXL"]
count = list(map(int, input().split()))

k = int(input())

for _ in range(k):
    preferred = input().strip()
    idx = sizes.index(preferred)

    best = -1
    best_dist = float('inf')

    for i in range(5):
        if count[i] == 0:
            continue

        dist = abs(i - idx)

        if dist < best_dist or (dist == best_dist and i > best):
            best = i
            best_dist = dist

    print(sizes[best])
    count[best] -= 1