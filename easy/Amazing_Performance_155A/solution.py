n = int(input())
scores = list(map(int, input().split()))

best = worst = scores[0]
amazing = 0

for score in scores[1:]:
    if score > best:
        amazing += 1
        best = score
    elif score < worst:
        amazing += 1
        worst = score

print(amazing)