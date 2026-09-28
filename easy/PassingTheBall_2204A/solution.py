import sys

def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        s = input().strip()

        visited = [False] * n
        pos = 0
        ans = 0

        while not visited[pos]:
            visited[pos] = True
            ans += 1

            if s[pos] == 'R':
                pos += 1
            else:
                pos -= 1

        print(ans)

if __name__ == "__main__":
    solve()