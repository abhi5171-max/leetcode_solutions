from collections import Counter

s = input().strip()
k = int(input())

freq = Counter(s)

# Characters sorted by frequency
chars = sorted(freq.keys(), key=lambda ch: freq[ch])

removed = set()

for ch in chars:
    if freq[ch] <= k:
        k -= freq[ch]
        removed.add(ch)
    else:
        break

# Build the resulting subsequence
result = ''.join(ch for ch in s if ch not in removed)

print(len(set(result)))
print(result)