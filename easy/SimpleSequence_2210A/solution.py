import sys

def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        print(*range(n, 0, -1))


if __name__ == "__main__":
    solve()