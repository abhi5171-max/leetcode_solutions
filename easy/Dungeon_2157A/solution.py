from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    freq = Counter(a)
    k = min(freq.values())

    deletions = sum(count - min(count, k) for count in freq.values())

    print(deletions)