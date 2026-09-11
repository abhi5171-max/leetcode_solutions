import sys


def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n, m = map(int, input().split())

        # Store first letters of all initial words
        available = set()

        for _ in range(n):
            word = input().strip()
            available.add(word[0].upper())

        possible = True

        # Check every abbreviation
        for _ in range(m):
            abbreviation = input().strip()

            for char in abbreviation:
                if char not in available:
                    possible = False

        print("YES" if possible else "NO")


if __name__ == "__main__":
    solve()