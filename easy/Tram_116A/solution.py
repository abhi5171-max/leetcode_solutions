n = int(input())

current = 0
capacity = 0

for _ in range(n):
    a, b = map(int, input().split())
    current -= a
    current += b
    capacity = max(capacity, current)

print(capacity)