t = int(input())

for _ in range(t):
    a, b, c, d = map(int, input().split())

    first_half = max(a, b) <= 2 * (min(a, b) + 1)

    r = c - a
    k = d - b

    second_half = max(r, k) <= 2 * (min(r, k) + 1)

    if first_half and second_half:
        print("YES")
    else:
        print("NO")