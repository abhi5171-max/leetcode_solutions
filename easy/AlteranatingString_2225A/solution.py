import sys


def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        s = input().strip()

        bad = 0

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                bad += 1

        if bad <= 2:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()