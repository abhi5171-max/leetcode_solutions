n = int(input())

best = None

for b in range(n // 7 + 1):
    remaining = n - 7 * b

    if remaining >= 0 and remaining % 4 == 0:
        a = remaining // 4
        candidate = '4' * a + '7' * b

        if best is None or len(candidate) < len(best):
            best = candidate

print(best if best is not None else -1)