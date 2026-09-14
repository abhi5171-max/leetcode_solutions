t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    # First set bit costs 1 for each number
    answer = min(n, k)
    n -= answer

    # Additional set bits have costs: 1, 2, 4, 8, ...
    cost = 1

    while n >= cost:
        count = min(k, n // cost)
        answer += count
        n -= count * cost
        cost *= 2

    print(answer)