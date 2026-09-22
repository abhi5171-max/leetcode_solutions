import sys


def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        x, y = map(int, input().split())

        if y // x > 2:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()