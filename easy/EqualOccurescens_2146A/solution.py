
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    freq = []

    i = 0
    while i < n:
        j = i

        while j < n and a[j] == a[i]:
            j += 1

        freq.append(j - i)
        i = j

    freq.sort()

    ans = 0
    k = len(freq)

    for i in range(k):
        ans = max(ans, freq[i] * (k - i))

    print(ans)
