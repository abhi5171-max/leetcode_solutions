# 🐉 A. Dragons

## 📌 Problem

Kirito is stuck on a level in an MMORPG and needs to defeat all `n` dragons to move to the next level.

Kirito starts with strength `s`. Each dragon has:

* `xi` — Dragon's strength
* `yi` — Bonus strength Kirito receives after defeating the dragon

Kirito can defeat a dragon only if:

```text
Kirito's Strength > Dragon's Strength
```

After defeating a dragon, Kirito's strength increases by `yi`.

The goal is to determine whether Kirito can defeat all dragons without losing.

---

## 💡 Approach

The best strategy is to fight the dragons in increasing order of their strength.

### Steps

1. Store all dragons as `(strength, bonus)` pairs.
2. Sort the dragons based on their strength.
3. Traverse each dragon:

   * If Kirito's strength is less than or equal to the dragon's strength, print `NO`.
   * Otherwise, defeat the dragon and add the bonus strength.
4. If all dragons are defeated, print `YES`.

---

## 💻 Solution

```python
s, n = map(int, input().split())

dragons = []

for _ in range(n):
    x, y = map(int, input().split())
    dragons.append((x, y))

# Sort dragons by strength
dragons.sort()

for x, y in dragons:
    if s <= x:
        print("NO")
        break
    s += y
else:
    print("YES")
```

---

## ⏱️ Complexity

| Operation  | Complexity |
| ---------- | ---------- |
| Sorting    | O(n log n) |
| Traversing | O(n)       |
| Total      | O(n log n) |

---

## 📝 Example

### Input

```text
2 2
1 99
100 0
```

### Output

```text
YES
