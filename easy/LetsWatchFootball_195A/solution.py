a, b, c = map(int, input().split())

answer = (c * (a - b) + b - 1) // b

print(answer)