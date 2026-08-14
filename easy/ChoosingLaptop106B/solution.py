n = int(input())

laptops = []

for i in range(n):
    speed, ram, hdd, cost = map(int, input().split())
    laptops.append((speed, ram, hdd, cost, i + 1))

best_cost = float('inf')
best_index = -1

for i in range(n):
    speed, ram, hdd, cost, index = laptops[i]

    outdated = False

    for j in range(n):
        if i == j:
            continue

        speed2, ram2, hdd2, _, _ = laptops[j]

        if speed2 > speed and ram2 > ram and hdd2 > hdd:
            outdated = True
            break

    if not outdated and cost < best_cost:
        best_cost = cost
        best_index = index

print(best_index)