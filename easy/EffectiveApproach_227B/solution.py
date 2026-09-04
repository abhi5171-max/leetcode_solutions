n = int(input())
a = list(map(int, input().split()))

# pos[x] = position of value x in the permutation
pos = [0] * (n + 1)

for i in range(n):
    pos[a[i]] = i + 1

m = int(input())
queries = list(map(int, input().split()))

vasya = 0
petya = 0

for x in queries:
    p = pos[x]

    # Search from left
    vasya += p

    # Search from right
    petya += n - p + 1

print(vasya, petya)