n = int(input())
times = list(map(int, input().split()))

minimum = min(times)

if times.count(minimum) == 1:
    print(times.index(minimum) + 1)
else:
    print("Still Rozdil")