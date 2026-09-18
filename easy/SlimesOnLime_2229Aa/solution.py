import sys


def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        mn = min(a)
        mx = max(a)

        ans = (mx - mn + 1) // 2

        print(ans)


if __name__ == "__main__":
    solve()