
t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    ones = s.count('1')

    ans = n + (n - 2) * ones

    print(ans)
