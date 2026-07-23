n = int(input())

unique_leaves = set()

for _ in range(n):
    species, color = input().split()
    unique_leaves.add((species, color))

print(len(unique_leaves))