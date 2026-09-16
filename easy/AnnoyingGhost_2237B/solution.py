
import sys

input = sys.stdin.readline


def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        mn = a[0]
        ans = 0

        for x in a:
            mn = min(mn, x)
            ans += mn

        print(ans)


if __name__ == "__main__":
    solve()
