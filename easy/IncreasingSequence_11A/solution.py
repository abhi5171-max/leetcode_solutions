n, d = map(int, input().split())
b = list(map(int, input().split()))

moves = 0

for i in range(1, n):
    if b[i] <= b[i - 1]:
        diff = b[i - 1] - b[i] + 1
        k = (diff + d - 1) // d  # Ceiling division
        moves += k
        b[i] += k * d

print(moves)