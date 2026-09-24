import sys

def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n, c, k = map(int, input().split())
        a = sorted(map(int, input().split()))

        for x in a:
            if x <= c:
                c += x
            else:
                break

        print(c)


if __name__ == "__main__":
    solve()