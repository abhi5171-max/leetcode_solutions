t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    maximum = max(a)
    answer = a.count(maximum)

    print(answer)