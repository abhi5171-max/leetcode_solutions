k = int(input())
l = int(input())

count = 0

while l % k == 0:
    l //= k
    count += 1

if l == 1:
    print("YES")
    print(count - 1)
else:
    print("NO")