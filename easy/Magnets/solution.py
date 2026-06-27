n = int(input())

groups = 1
prev = input()

for _ in range(n - 1):
    curr = input()
    if curr != prev:
        groups += 1
    prev = curr

print(groups)