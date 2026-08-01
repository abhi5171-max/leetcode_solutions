names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]

n = int(input())

group = 1

while n > 5 * group:
    n -= 5 * group
    group *= 2

print(names[(n - 1) // group])