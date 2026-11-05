t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    count = [0] * k

    for i in range(n):
        if s[i] == '1':
            count[i % k] += 1

    if all(x % 2 == 0 for x in count):
        print("YES")
    else:
        print("NO")