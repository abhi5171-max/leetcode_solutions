from collections import Counter

k = int(input())
s = input().strip()

freq = Counter(s)
base = []

for ch in sorted(freq):
    if freq[ch] % k != 0:
        print(-1)
        break
    base.append(ch * (freq[ch] // k))
else:
    print(''.join(base) * k)