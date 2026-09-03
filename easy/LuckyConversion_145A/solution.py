a = input().strip()
b = input().strip()

cnt47 = 0
cnt74 = 0

for x, y in zip(a, b):
    if x == '4' and y == '7':
        cnt47 += 1
    elif x == '7' and y == '4':
        cnt74 += 1

print(max(cnt47, cnt74))