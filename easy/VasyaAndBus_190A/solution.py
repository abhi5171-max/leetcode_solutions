n, m = map(int, input().split())

if n == 0 and m > 0:
    print("Impossible")
else:
    minimum = n + max(0, m - n)
    maximum = n + max(0, m - 1)

    print(minimum, maximum)