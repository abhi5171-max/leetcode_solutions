
n = int(input())
a = list(map(int, input().split()))

chest = sum(a[0::3])
biceps = sum(a[1::3])
back = sum(a[2::3])

if chest > biceps and chest > back:
    print("chest")
elif biceps > chest and biceps > back:
    print("biceps")
else:
    print("back")
