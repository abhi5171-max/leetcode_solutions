l, r = map(int, input().split())

lucky = []


def generate(x):
    if x > 10**10:
        return

    if x:
        lucky.append(x)

    generate(x * 10 + 4)
    generate(x * 10 + 7)


generate(0)
lucky.sort()

ans = 0
current = l

for x in lucky:
    if x < l:
        continue

    if current > r:
        break

    end = min(r, x)

    # Every number from current to end has next(number) = x
    ans += (end - current + 1) * x

    current = end + 1

    if current > r:
        break

print(ans)