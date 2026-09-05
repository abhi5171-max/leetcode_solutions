n, k = map(int, input().split())
a = list(map(int, input().split()))

# Store (requested_segment, child_index)
children = [(a[i], i) for i in range(k)]

# Process requested segments from largest to smallest
children.sort(reverse=True)

used = [False] * (n * k + 1)
ans = [[] for _ in range(k)]

for value, child in children:
    # Give the requested segment
    ans[child].append(value)
    used[value] = True

    # Give n-1 unused smaller segments
    current = value - 1

    while len(ans[child]) < n:
        if not used[current]:
            ans[child].append(current)
            used[current] = True

        current -= 1

# Print answer
for child in range(k):
    print(*ans[child])