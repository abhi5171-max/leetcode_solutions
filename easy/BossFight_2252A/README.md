# A. Boss Fight

## Problem

You have `n` spell cards, where the `i-th` card deals `ai` damage.

You can play the cards in any order.

However, if two consecutive cards deal the same damage:

* Both cards deal their normal damage.
* The shield permanently activates.
* All remaining cards deal `0` damage.

Find the maximum total damage you can deal by arranging the cards optimally.

---

## Approach

To avoid activating the shield, we should arrange cards so that no two consecutive cards have the same damage.

Let:

* `max_freq` = frequency of the most common damage value.
* `other_count` = number of all remaining cards.

We can use cards with different values as separators between the most frequent cards.

### Case 1: All cards can be used

If:

```text
max_freq <= other_count + 1
```

we can arrange all cards without placing two equal cards consecutively.

Therefore:

```text
answer = sum(a)
```

### Case 2: Some cards cannot be used

If the most frequent card appears too many times, eventually two equal cards must be played consecutively.

Since the card that triggers the shield still deals damage, we can use:

```text
other_count + 2
```

copies of the most frequent card.

The remaining copies will deal `0` damage.

---

## Python Solution

```python
from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    freq = Counter(a)

    max_val = max(freq, key=freq.get)
    max_freq = freq[max_val]

    total_sum = sum(a)
    other_count = n - max_freq

    if max_freq <= other_count + 1:
        print(total_sum)
    else:
        usable_max = other_count + 2

        answer = total_sum - (max_freq - usable_max) * max_val
        print(answer)
```

## Complexity Analysis

For each test case:

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

## Key Idea

Use different cards as separators between identical cards. If identical cards eventually become consecutive, the second card still deals damage, so one additional duplicate card can be counted before the shield activates.
