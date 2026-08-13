n = int(input())

best_handle = ""
best_score = float("-inf")

for _ in range(n):
    data = input().split()

    handle = data[0]
    plus = int(data[1])
    minus = int(data[2])

    problem_points = sum(map(int, data[3:8]))

    score = problem_points + plus * 100 - minus * 50

    if score > best_score:
        best_score = score
        best_handle = handle

print(best_handle)