import sys

def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        x = int(input())

        if x < 67:
            print(x + 1)
        else:
            print(67)

if __name__ == "__main__":
    solve()