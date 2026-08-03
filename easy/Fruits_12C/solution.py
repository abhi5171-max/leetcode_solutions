from collections import Counter

n, m = map(int, input().split())
prices = list(map(int, input().split()))

freq = Counter()
for _ in range(m):
    fruit = input().strip()
    freq[fruit] += 1

counts = sorted(freq.values())
prices.sort()

# Minimum cost:
# Highest frequency gets lowest price
min_cost = sum(c * p for c, p in zip(sorted(counts, reverse=True), prices))

# Maximum cost:
# Highest frequency gets highest price
max_cost = sum(c * p for c, p in zip(sorted(counts, reverse=True), sorted(prices, reverse=True)))

print(min_cost, max_cost)