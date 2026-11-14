
t = int(input())

for _ in range(t):
    n = input().strip()
    print(min(int(digit) for digit in n))
