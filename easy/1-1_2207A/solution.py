import sys

def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        s = input().strip()

        minimum = 0
        maximum = s.count('1')

        i = 0

        while i < n:
            if s[i] == '1':
                j = i

                while j < n and s[j] == '1':
                    j += 1

                length = j - i

                # Minimum contribution of this 1-run
                minimum += (length + 2) // 2

                i = j

            else:
                j = i

                while j < n and s[j] == '0':
                    j += 1

                length = j - i

                # A single zero between two 1s can become 1
                if length == 1 and i > 0 and j < n:
                    maximum += 1

                i = j

        print(minimum, maximum)


if __name__ == "__main__":
    solve()