n = int(input())
coins = list(map(int, input().split()))

coins.sort(reverse=True)

total_sum = sum(coins)
picked_sum = 0
count = 0

for coin in coins:
    picked_sum += coin
    count += 1
    if picked_sum > total_sum - picked_sum:
        break

print(count)