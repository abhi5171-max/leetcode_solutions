n, m, k = map(int, input().split())

min_viability = [10**18] * (m + 1)

for _ in range(n):
    r, c = map(int, input().split())
    min_viability[r] = min(min_viability[r], c)

total = sum(min_viability[1:])

print(min(k, total))