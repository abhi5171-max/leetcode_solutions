
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    total = sum(arr)
    zeros = arr.count(0)

    print(total + zeros)
