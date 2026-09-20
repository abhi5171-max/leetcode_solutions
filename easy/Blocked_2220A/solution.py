import sys

def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        if len(set(a)) == 1:
            print(-1)
        else:
            a.sort(reverse=True)
            print(*a)


if __name__ == "__main__":
    solve()