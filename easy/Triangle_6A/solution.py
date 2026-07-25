sticks = list(map(int, input().split()))

segment = False

for i in range(4):
    sides = [sticks[j] for j in range(4) if j != i]
    sides.sort()

    if sides[0] + sides[1] > sides[2]:
        print("TRIANGLE")
        exit()
    elif sides[0] + sides[1] == sides[2]:
        segment = True

if segment:
    print("SEGMENT")
else:
    print("IMPOSSIBLE")