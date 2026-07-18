n = int(input())

divisors = [0] * (n + 1)

for i in range(2, n + 1):
    if divisors[i] == 0:  # i is prime
        for j in range(i, n + 1, i):
            divisors[j] += 1

count = 0
for i in range(2, n + 1):
    if divisors[i] == 2:
        count += 1

print(count)