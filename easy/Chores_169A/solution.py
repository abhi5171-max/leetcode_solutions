n, a, b = map(int, input().split())
h = list(map(int, input().split()))

h.sort()

answer = h[b] - h[b - 1]

print(answer)