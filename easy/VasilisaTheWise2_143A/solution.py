r1, r2 = map(int, input().split())
c1, c2 = map(int, input().split())
d1, d2 = map(int, input().split())

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):

                # All numbers must be different
                if len({a, b, c, d}) != 4:
                    continue

                # Check all required sums
                if a + b != r1:
                    continue
                if c + d != r2:
                    continue
                if a + c != c1:
                    continue
                if b + d != c2:
                    continue
                if a + d != d1:
                    continue
                if b + c != d2:
                    continue

                print(a, b)
                print(c, d)
                exit()

print(-1)