import sys

def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        tokens = list(map(int, input().split()))
        rounds = 0

        while len(set(tokens)) == 3:
            max_index = tokens.index(max(tokens))
            min_index = tokens.index(min(tokens))

            tokens[max_index] -= 1
            tokens[min_index] += 1

            rounds += 1

        print(rounds)