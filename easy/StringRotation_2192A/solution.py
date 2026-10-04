import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    transitions = 0
    same = False

    for i in range(n):
        if s[i] != s[(i + 1) % n]:
            transitions += 1
        else:
            same = True

    if not same:
        # Every adjacent circular pair is different.
        print(n)
    else:
        # We can place an equal pair across the rotation boundary.
        print(transitions + 1)