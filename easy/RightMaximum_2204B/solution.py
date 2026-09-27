import sys

def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        mx = -1
        ans = 0

        for i in range(n - 1, -1, -1):
            if a[i] >= mx:
                mx = a[i]
                ans += 1

        print(ans)


if __name__ == "__main__":
    solve()