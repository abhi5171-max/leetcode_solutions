import sys


def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))

        total = sum(a)

        if total % 2 == 1 or (n * k) % 2 == 0:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()