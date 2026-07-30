n, v = map(int, input().split())

kayaks = []
catamarans = []

for i in range(1, n + 1):
    t, p = map(int, input().split())
    if t == 1:
        kayaks.append((p, i))
    else:
        catamarans.append((p, i))

kayaks.sort(reverse=True)
catamarans.sort(reverse=True)

pre_kayaks = [0]
for p, _ in kayaks:
    pre_kayaks.append(pre_kayaks[-1] + p)

pre_catamarans = [0]
for p, _ in catamarans:
    pre_catamarans.append(pre_catamarans[-1] + p)

best = 0
best_cats = 0
best_kayaks = 0

max_cats = min(len(catamarans), v // 2)

for c in range(max_cats + 1):
    remaining = v - 2 * c
    k = min(len(kayaks), remaining)
    total = pre_catamarans[c] + pre_kayaks[k]

    if total > best:
        best = total
        best_cats = c
        best_kayaks = k

print(best)

answer = []
for i in range(best_cats):
    answer.append(str(catamarans[i][1]))
for i in range(best_kayaks):
    answer.append(str(kayaks[i][1]))

print(" ".join(answer))