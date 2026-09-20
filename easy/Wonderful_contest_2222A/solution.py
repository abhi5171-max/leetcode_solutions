import sys

def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        if 100 in a:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    solve()