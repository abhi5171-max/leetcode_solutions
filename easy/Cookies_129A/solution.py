n = int(input())
a = list(map(int, input().split()))

total = sum(a)

if total % 2 == 0:
    answer = sum(1 for x in a if x % 2 == 0)
else:
    answer = sum(1 for x in a if x % 2 == 1)

print(answer)