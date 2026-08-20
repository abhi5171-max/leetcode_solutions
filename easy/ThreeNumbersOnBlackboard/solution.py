t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    a, b, c = sorted([a, b, c])

    answer = min(c - a, b)

    print(answer)