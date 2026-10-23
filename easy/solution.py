t = int(input())

for _ in range(t):
    n = int(input())
    s, t_name = input().split()

    if sorted(s) == sorted(t_name):
        print("YES")
    else:
        print("NO")