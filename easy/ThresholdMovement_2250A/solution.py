import sys


def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        # Directions must be:
        # Right, Left, Right, Left, ...
        # Therefore n must be even.
        if n % 2 == 1:
            print("NO")
            continue

        # 1-based odd positions must have a[i] > x
        # 1-based even positions must have a[i] < x

        # In 0-based indexing:
        # a[0], a[2], ... > x
        # a[1], a[3], ... < x

        min_odd = min(a[0::2])
        max_even = max(a[1::2])

        # Need:
        # max_even < x < min_odd
        #
        # x must be an integer.
        if max_even + 1 < min_odd:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()