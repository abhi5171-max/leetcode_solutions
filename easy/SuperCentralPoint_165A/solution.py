n = int(input())

points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

answer = 0

for x, y in points:
    left = right = upper = lower = False

    for x2, y2 in points:
        if y2 == y and x2 < x:
            left = True
        if y2 == y and x2 > x:
            right = True
        if x2 == x and y2 < y:
            lower = True
        if x2 == x and y2 > y:
            upper = True

    if left and right and upper and lower:
        answer += 1

print(answer)