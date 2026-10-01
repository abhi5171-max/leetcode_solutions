import sys


def digit_sum(n):
    return sum(map(int, str(n)))


def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        x = int(input())

        ans = 0

        for y in range(x + 1, x + 101):
            if y - digit_sum(y) == x:
                ans += 1

        print(ans)


if __name__ == "__main__":
    solve()