from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    freq = Counter(a)

    max_val = max(freq, key=lambda value: freq[value])
    max_freq = freq[max_val]

    total_sum = sum(a)
    other_count = n - max_freq

    if max_freq <= other_count + 1:
        print(total_sum)
    else:
        usable_max = other_count + 2

        answer = total_sum - (max_freq - usable_max) * max_val
        print(answer)