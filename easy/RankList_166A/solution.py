n, k = map(int, input().split())

teams = []

for _ in range(n):
    p, t = map(int, input().split())
    teams.append((p, t))

# Sort by:
# 1. Problems solved -> descending
# 2. Penalty time -> ascending
teams.sort(key=lambda x: (-x[0], x[1]))

# Get the team at the k-th position
target = teams[k - 1]

# Count teams with the same score
answer = teams.count(target)

print(answer)