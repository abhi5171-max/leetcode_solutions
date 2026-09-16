import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))

    answer = max(h) - min(h) + 1

    print(answer)