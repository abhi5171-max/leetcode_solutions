import sys

def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        a = list(map(int, input().split()))

        total = sum(a)
        maximum = max(a)

        answer = 2 * maximum - total

        print(answer)


if __name__ == "__main__":
    solve()