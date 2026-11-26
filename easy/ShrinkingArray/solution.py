
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # Case 1: Already beautiful
    beautiful = False

    for i in range(n - 1):
        if abs(a[i] - a[i + 1]) <= 1:
            beautiful = True
            break

    if beautiful:
        print(0)
        continue

    # Case 2: Check for a local maximum or minimum
    possible = False

    for i in range(1, n - 1):
        if (a[i] > a[i - 1] and a[i] > a[i + 1]) or \
           (a[i] < a[i - 1] and a[i] < a[i + 1]):
            possible = True
            break

    if possible:
        print(1)
    else:
        print(-1)
