n = int(input())
a = list(map(int, input().split()))

total = sum(a)

# If total petals are odd, take all flowers
if total % 2 == 1:
    print(total)
else:
    # Find the smallest odd number of petals
    smallest_odd = float('inf')

    for petals in a:
        if petals % 2 == 1:
            smallest_odd = min(smallest_odd, petals)

    if smallest_odd == float('inf'):
        print(0)
    else:
        print(total - smallest_odd)