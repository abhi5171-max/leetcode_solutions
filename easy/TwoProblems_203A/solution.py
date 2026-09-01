x, t, a, b, da, db = map(int, input().split())

# Solve neither problem
if x == 0:
    print("YES")
    exit()

# Possible scores from the first problem
scores_a = [a - i * da for i in range(t)]

# Possible scores from the second problem
scores_b = [b - i * db for i in range(t)]

# Solve only the first problem
if x in scores_a:
    print("YES")
    exit()

# Solve only the second problem
if x in scores_b:
    print("YES")
    exit()

# Solve both problems
for score_a in scores_a:
    for score_b in scores_b:
        if score_a + score_b == x:
            print("YES")
            exit()

print("NO")