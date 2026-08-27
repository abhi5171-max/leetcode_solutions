# Petr and Book

## Problem Statement

Petr has bought a book containing `n` pages. Starting from Monday, he reads as many pages as possible each day according to his weekly schedule.

The number of pages Petr can read on each day is given for:

1. Monday
2. Tuesday
3. Wednesday
4. Thursday
5. Friday
6. Saturday
7. Sunday

Determine the day of the week on which Petr will finish reading the book.

---

## Approach

The reading schedule repeats every 7 days.

### Steps

1. Read the number of pages `n`.
2. Store the pages Petr can read each day in an array.
3. Calculate the total number of pages he can read in one week.
4. Use `n % weekly_pages` to remove complete weeks.
5. If the remainder is `0`, set it to the total weekly pages because Petr finishes on the corresponding day of a full week.
6. Iterate through the seven days:

   * Subtract that day's pages from `n`.
   * When `n <= 0`, Petr has finished the book.
7. Print the corresponding day number.

---

## Python Implementation

```python
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
```

## Example

### Input

```text
100
15 20 20 15 10 30 45
```

### Calculation

Pages read in one week:

```text
15 + 20 + 20 + 15 + 10 + 30 + 45 = 155
```

Since the book has 100 pages, Petr finishes within the first week.

| Day       | Pages Remaining |
| --------- | --------------: |
| Monday    |              85 |
| Tuesday   |              65 |
| Wednesday |              45 |
| Thursday  |              30 |
| Friday    |              20 |
| Saturday  |             -10 |

Petr finishes on **Saturday**, which is day `6`.

### Output

```text
6
```

---

## Complexity

* **Time Complexity:** `O(7)` → `O(1)`
* **Space Complexity:** `O(7)` → `O(1)`

## Key Concept

The main idea is to **skip complete weeks using modulo** and then simulate only the remaining days.
