n = int(input())
days = list(map(int, input().split()))

# Total pages Petr can read in one week
week = sum(days)

# Remove complete weeks
n %= week

# If exactly divisible, the book finishes
# on the last required day of a full week
if n == 0:
    n = week

# Find the finishing day
for i in range(7):
    n -= days[i]

    if n <= 0:
        print(i + 1)
        break