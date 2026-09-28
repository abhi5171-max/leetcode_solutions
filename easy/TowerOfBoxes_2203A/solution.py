import sys

def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n, w, d = map(int, input().split())

        max_boxes = d // w + 1

        towers = (n + max_boxes - 1) // max_boxes

        print(towers)

if __name__ == "__main__":
    solve()