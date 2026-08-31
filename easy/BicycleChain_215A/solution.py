n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

max_ratio = 0
count = 0

for x in a:
    for y in b:
        if y % x == 0:
            ratio = y // x

            if ratio > max_ratio:
                max_ratio = ratio
                count = 1
            elif ratio == max_ratio:
                count += 1

print(count)