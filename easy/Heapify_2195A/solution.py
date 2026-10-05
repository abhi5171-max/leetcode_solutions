def odd_part(x):
    while x % 2 == 0:
        x //= 2
    return x


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    possible = True

    for i in range(n):
        # Convert 0-based index to 1-based index
        index = i + 1

        if odd_part(index) != odd_part(a[i]):
            possible = False
            break

    print("YES" if possible else "NO")