# A. Testing Pants for Sadness

## Problem

A test contains `n` questions.

- Question `i` has `a[i]` answer choices.
- Exactly one answer is correct.
- If a wrong answer is selected, the test restarts from Question 1.
- Previously discovered correct answers are remembered.

Find the minimum number of clicks required in the **worst case**.

---

## Approach

For every question:

- Before reaching it, all previous correct answers must be clicked again.
- In the worst case, all incorrect options are tried first.
- Each wrong attempt requires:
  - Re-answering all previous questions.
  - Clicking one wrong option.
- Finally, one click selects the correct answer.

If `passed` questions are already known:

```
Contribution =
(a[i] - 1) × (passed + 1) + 1
```

where:
- `(a[i] - 1)` = wrong attempts
- `(passed + 1)` = clicks needed per wrong attempt
- `+1` = final correct click

---

## Algorithm

1. Initialize answer as `0`.
2. For every question:
   - Add `(a[i]-1) * (passed+1) + 1`.
   - Increase `passed`.
3. Print the total.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

---

## Key Insight

Each incorrect answer forces restarting the exam, meaning all previously solved questions must be clicked again before attempting the current question.

---

## Python Solution

```python
n = int(input())
a = list(map(int, input().split()))

clicks = 0
passed = 0

for x in a:
    clicks += (x - 1) * (passed + 1) + 1
    passed += 1

print(clicks)
```