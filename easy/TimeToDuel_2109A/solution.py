
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if 0 in a and "00" in "".join(map(str, a)):
        print("YES")
    elif sum(a) == n:
        print("YES")
    else:
        print("NO")
