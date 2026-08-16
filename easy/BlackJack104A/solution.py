n = int(input())

required = n - 10

if 2 <= required <= 9:
    print(4)
elif required == 10:
    print(15)
elif required == 1 or required == 11:
    print(4)
else:
    print(0)