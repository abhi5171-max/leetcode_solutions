n = int(input())
a = list(map(int, input().split()))

clicks = 0
passed = 0

for x in a:
    clicks += (x - 1) * (passed + 1) + 1
    passed += 1