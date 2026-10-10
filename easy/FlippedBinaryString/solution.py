
t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    ones = [i + 1 for i in range(n) if s[i] == '1']
    zeros = [i + 1 for i in range(n) if s[i] == '0']

    if len(ones) % 2 == 0:
        print(len(ones))
        print(*ones)
    elif len(zeros) % 2 == 1:
        print(len(zeros))
        print(*zeros)
    else:
        print(-1)
