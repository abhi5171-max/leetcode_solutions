import sys

def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        operations = []

        # Process levels from k down to 1
        for level in range(k, 0, -1):

            # Find all courses currently at this level
            for i in range(n):
                if b[i] == level:
                    # Move course to level + 1
                    b[i] += 1
                    operations.append(i + 1)

        if len(operations) <= 1000:
            print(len(operations))
            if operations:
                print(*operations)
        else:
            print(-1)


if __name__ == "__main__":
    solve()