a, b, c = map(int, input().split())

if max(a, b, c) - min(a, b, c) >= 10:
    print("check again")
else:
    scores = sorted([a, b, c])
    print("final", scores[1])