import sys

MOD = 676767677


def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        ans = 0
        last_greater = -1

        for i, x in enumerate(a):
            if x > 1:
                ans += x
                last_greater = i

        # All elements are 1
        if last_greater == -1:
            print(1)
            continue

        # There is at least one 1 after the last element > 1
        if last_greater < n - 1:
            ans += 1

        print(ans % MOD)


if __name__ == "__main__":
    solve()