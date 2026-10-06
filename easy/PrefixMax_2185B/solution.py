t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    def get_value(arr):
        current_max = 0
        total = 0

        for x in arr:
            current_max = max(current_max, x)
            total += current_max

        return total

    # Value without performing a swap
    ans = get_value(a)

    # Try every possible swap
    for i in range(n):
        for j in range(i + 1, n):
            a[i], a[j] = a[j], a[i]

            ans = max(ans, get_value(a))

            # Restore the original array
            a[i], a[j] = a[j], a[i]

    print(ans)