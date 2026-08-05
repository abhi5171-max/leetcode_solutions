s = input()
target = "hello"

j = 0

for c in s:
    if j < len(target) and c == target[j]:
        j += 1

if j == len(target):
    print("YES")
else:
    print("NO")