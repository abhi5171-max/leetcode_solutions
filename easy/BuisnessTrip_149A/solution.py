k = int(input())
growth = list(map(int, input().split()))

if k == 0:
    print(0)
    exit()

growth.sort(reverse=True)

total = 0
months = 0

for g in growth:
    total += g
    months += 1
    if total >= k:
        print(months)
        exit()

print(-1)