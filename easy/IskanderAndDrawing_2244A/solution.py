t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    max_length = 0
    current_length = 0

    for char in s:
        if char == '#':
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0

    print((max_length + 1) // 2)