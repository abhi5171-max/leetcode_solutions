t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if all(a[i] <= a[i + 1] for i in range(n - 1)):
        print(n)
    else:
        print(1)