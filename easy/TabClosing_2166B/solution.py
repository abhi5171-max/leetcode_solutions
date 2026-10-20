
t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    if a // c == b:
        print(1)
    else:
        print(2)
