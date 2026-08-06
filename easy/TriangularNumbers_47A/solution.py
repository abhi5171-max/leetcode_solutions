n = int(input())

total = 0
i = 1

while total < n:
    total += i
    i += 1

if total == n:
    print("YES")
else:
    print("NO")