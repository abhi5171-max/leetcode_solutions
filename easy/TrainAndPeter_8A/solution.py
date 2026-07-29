s = input().strip()
a = input().strip()
b = input().strip()

def check(text, first, second):
    pos1 = text.find(first)
    if pos1 == -1:
        return False
    pos2 = text.find(second, pos1 + len(first))
    return pos2 != -1

forward = check(s, a, b)
backward = check(s[::-1], a, b)

if forward and backward:
    print("both")
elif forward:
    print("forward")
elif backward:
    print("backward")
else:
    print("fantasy")