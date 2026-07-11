n = int(input())
numbers = list(map(int, input().split()))

even = sum(1 for x in numbers if x % 2 == 0)
odd = n - even

for i, x in enumerate(numbers):
    if (even > odd and x % 2 == 1) or (odd > even and x % 2 == 0):
        print(i + 1)
        break