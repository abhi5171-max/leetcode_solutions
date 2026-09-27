import sys

def solve():
    input = sys.stdin.readline
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        pos = a.index(n)

        a[0], a[pos] = a[pos], a[0]

        print(*a)


if __name__ == "__main__":
    solve()