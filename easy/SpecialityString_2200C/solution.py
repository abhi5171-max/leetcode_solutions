t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    stack = []

    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    if len(stack) == 0:
        print("YES")
    else:
        print("NO")