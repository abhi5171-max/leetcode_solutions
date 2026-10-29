
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    operations = 0
    negative_count = 0

    for x in a:
        if x == 0:
            operations += 1
        elif x == -1:
            negative_count += 1

    if negative_count % 2 == 1:
        operations += 2

    print(operations)
