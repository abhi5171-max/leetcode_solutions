import sys


def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        w = list(map(int, input().split()))

        count0 = w.count(0)
        count1 = w.count(1)
        count2 = w.count(2)

        # Every zero can be removed individually.
        ans = count0

        # Pair 1 and 2: 1 + 2 = 3.
        pairs = min(count1, count2)
        ans += pairs

        count1 -= pairs
        count2 -= pairs

        # Three 1s or three 2s have sums divisible by 3.
        ans += count1 // 3
        ans += count2 // 3

        print(ans)


if __name__ == "__main__":
    solve()