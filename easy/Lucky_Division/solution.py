n = int(input())

lucky_numbers = []

for i in range(1, 1001):
    if all(c in "47" for c in str(i)):
        lucky_numbers.append(i)

for num in lucky_numbers:
    if n % num == 0:
        print("YES")
        break
else:
    print("NO")