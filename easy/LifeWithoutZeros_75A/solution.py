def remove_zeros(n):
    return int(str(n).replace('0', ''))

a = int(input())
b = int(input())

c = a + b

if remove_zeros(a) + remove_zeros(b) == remove_zeros(c):
    print("YES")
else:
    print("NO")