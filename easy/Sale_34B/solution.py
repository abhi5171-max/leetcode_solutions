n, m = map(int, input().split())
prices = list(map(int, input().split()))

prices.sort()

earn = 0
for i in range(min(m, n)):
    if prices[i] < 0:
        earn += -prices[i]
    else:
        break

print(earn)