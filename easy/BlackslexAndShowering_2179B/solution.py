
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    total = sum(abs(a[i] - a[i - 1]) for i in range(1, n))
    max_reduction = 0

    for i in range(n):
        if i == 0:
            reduction = abs(a[1] - a[0])
        elif i == n - 1:
            reduction = abs(a[n - 1] - a[n - 2])
        else:
            reduction = (
                abs(a[i] - a[i - 1])
                + abs(a[i + 1] - a[i])
                - abs(a[i + 1] - a[i - 1])
            )

        max_reduction = max(max_reduction, reduction)

    print(total - max_reduction)
