lines = []
try:
    while True:
        lines.append(input())
except EOFError:
    pass

width = max(len(line) for line in lines)

print("*" * (width + 2))

left_turn = True

for line in lines:
    diff = width - len(line)

    if diff % 2 == 0:
        left = right = diff // 2
    else:
        if left_turn:
            left = diff // 2
            right = diff - left
        else:
            right = diff // 2
            left = diff - right
        left_turn = not left_turn

    print("*" + " " * left + line + " " * right + "*")

print("*" * (width + 2))