t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    x = a[0]
    pos = -1

    # Find the first decrease or equal adjacent element
    for i in range(1, m):
        if a[i] <= a[i - 1]:
            pos = i
            break

    if pos == -1:
        # Pattern must be consecutive increasing numbers
        if all(a[i] == x + i for i in range(m)):
            print(max(0, n - x - m + 2))
        else:
            print(0)

    else:
        # Determine the starting block
        k = x + pos - 1

        if k > n:
            print(0)
            continue

        block = k
        val = x
        match = True

        # Verify the pattern
        for j in range(m):
            if val != a[j]:
                match = False
                break

            if val == block:
                block += 1
                val = 1
            else:
                val += 1

        print(1 if match else 0)