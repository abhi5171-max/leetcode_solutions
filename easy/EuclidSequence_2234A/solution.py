import sys
from collections import Counter

input = sys.stdin.readline


def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))

        # The first two elements must be the two largest.
        b.sort(reverse=True)

        x = b[0]
        y = b[1]

        # Count remaining elements.
        cnt = Counter(b)

        # Remove x and y.
        cnt[x] -= 1
        cnt[y] -= 1

        possible = True

        while y > 0:
            r = x % y

            # Remainder must be positive.
            if r == 0:
                break

            # Remainder must exist in the input.
            if cnt[r] == 0:
                possible = False
                break

            cnt[r] -= 1

            x, y = y, r

        # All elements must have been used.
        if possible and sum(cnt.values()) == 0:
            print(b[0], b[1])
        else:
            print(-1)


if __name__ == "__main__":
    solve()