n = int(input())

left_open = 0
right_open = 0

for _ in range(n):
    l, r = map(int, input().split())
    left_open += l
    right_open += r

left_closed = n - left_open
right_closed = n - right_open

print(min(left_open, left_closed) + min(right_open, right_closed))