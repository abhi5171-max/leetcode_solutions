import sys

def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        p = list(map(int, input().split()))

        if n == 1:
            print(1)
        else:
            print(*([2] * n))


if __name__ == "__main__":
    solve()