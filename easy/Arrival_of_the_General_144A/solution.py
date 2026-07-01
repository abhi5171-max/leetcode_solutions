n = int(input())
heights = list(map(int, input().split()))

max_height = max(heights)
min_height = min(heights)

# Leftmost occurrence of the maximum height
max_index = heights.index(max_height)

# Rightmost occurrence of the minimum height
min_index = n - 1 - heights[::-1].index(min_height)

moves = max_index + (n - 1 - min_index)

# If the maximum soldier crosses the minimum soldier
if max_index > min_index:
    moves -= 1

print(moves)