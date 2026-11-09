t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))

    print(len(set(b)))