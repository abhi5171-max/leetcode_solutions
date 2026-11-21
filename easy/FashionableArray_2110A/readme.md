
t = int(input())

for _ in range(t):
    n = int(input())
    a = sorted(map(int, input().split()))

    first_even = -1
    last_even = -1
    first_odd = -1
    last_odd = -1

    for i in range(n):
        if a[i] % 2 == 0:
            if first_even == -1:
                first_even = i
            last_even = i
        else:
            if first_odd == -1:
                first_odd = i
            last_odd = i

    even_count = last_even - first_even + 1 if first_even != -1 else 0
    odd_count = last_odd - first_odd + 1 if first_odd != -1 else 0

    print(n - max(even_count, odd_count))
