t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    freq = [0] * 102

    for x in a:
        freq[x] += 1

    for i in range(102):
        if freq[i] < 2:
            print(i)
            break