t = int(input())

for _ in range(t):
    n = int(input())

    if n < 3:
        print(n)
    elif n % 6 == 0:
        print(0)
    else:
        print(1 if n % 3 != 0 else 3)