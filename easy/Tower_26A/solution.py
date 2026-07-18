n = int(input())
bars = list(map(int, input().split()))

freq = {}

for bar in bars:
    freq[bar] = freq.get(bar, 0) + 1

max_height = max(freq.values())
total_towers = len(freq)

print(max_height, total_towers)