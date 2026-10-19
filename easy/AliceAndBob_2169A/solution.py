
t = int(input())

for _ in range(t):
    n, a = map(int, input().split())
    v = list(map(int, input().split()))

    less = sum(x < a for x in v)
    greater = sum(x > a for x in v)

    if greater >= less:
        print(a + 1)
    else:
        print(a - 1)
