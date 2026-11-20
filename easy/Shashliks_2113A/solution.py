
def cook(k, required, drop):
    if k < required:
        return 0, k

    count = (k - required) // drop + 1
    k -= count * drop

    return count, k


t = int(input())

for _ in range(t):
    k, a, b, x, y = map(int, input().split())

    # Order 1: First type, then second type
    count1, temp1 = cook(k, a, x)
    count2, temp2 = cook(temp1, b, y)
    total1 = count1 + count2

    # Order 2: Second type, then first type
    count3, temp3 = cook(k, b, y)
    count4, temp4 = cook(temp3, a, x)
    total2 = count3 + count4

    print(max(total1, total2))
