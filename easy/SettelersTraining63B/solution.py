n, k = map(int, input().split())
soldiers = list(map(int, input().split()))

coins = 0

while True:
    ranks = set()

    # Find all distinct ranks below k
    for rank in soldiers:
        if rank < k:
            ranks.add(rank)

    # If no soldier can be trained, everyone is rank k
    if not ranks:
        break

    # One soldier from every distinct rank gets promoted
    for rank in ranks:
        for i in range(n):
            if soldiers[i] == rank:
                soldiers[i] += 1
                break

    coins += 1

print(coins)