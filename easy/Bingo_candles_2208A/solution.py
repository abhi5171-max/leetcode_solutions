import sys

def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())

        freq = {}

        for _ in range(n):
            row = map(int, input().split())
            for x in row:
                freq[x] = freq.get(x, 0) + 1

        mx = max(freq.values())

        if mx <= n * n - n:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()