import sys


def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        distinct = len(set(a))
        print(distinct // 2)


if __name__ == "__main__":
    solve()