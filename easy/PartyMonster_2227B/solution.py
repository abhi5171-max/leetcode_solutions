import sys

def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        s = input().strip()

        if s.count('(') == s.count(')'):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()