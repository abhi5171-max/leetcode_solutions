import sys


def ceil_div(a, b):
    return (a + b - 1) // b


def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n, x, y, z = map(int, input().split())

        # Option 1: No AI
        without_ai = ceil_div(n, x + y)

        # Option 2: Use AI
        # Maxim works alone during AI setup.
        if x * z >= n:
            with_ai = ceil_div(n, x)
        else:
            remaining = n - x * z
            with_ai = z + ceil_div(remaining, x + 10 * y)

        print(min(without_ai, with_ai))


if __name__ == "__main__":
    solve()