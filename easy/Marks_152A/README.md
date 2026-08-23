# A. Marks — Codeforces

## Problem Statement

Given a gradebook of `n` students and `m` subjects, each student receives a mark from `1` to `9` in every subject.

A student is considered **successful** if they have the highest mark in **at least one subject**.

The task is to determine the number of successful students.

---

## Approach

For every subject:

1. Find the maximum mark obtained by any student.
2. Check which students received this maximum mark.
3. Mark those students as successful.
4. At the end, count the number of unique successful students.

A `set` is used to ensure that a student who is best in multiple subjects is counted only once.

### Example

For:

```text
3 3
223
232
112
```

* Subject 1 → maximum = `2` → Students 1 and 2
* Subject 2 → maximum = `3` → Student 2
* Subject 3 → maximum = `3` → Student 1

Therefore, there are **2 successful students**.

---

## Python 3 Solution

```python
n, m = map(int, input().split())

marks = [input().strip() for _ in range(n)]

successful = set()

for j in range(m):
    maximum = max(marks[i][j] for i in range(n))

    for i in range(n):
        if marks[i][j] == maximum:
            successful.add(i)

print(len(successful))
```

---

## Complexity Analysis

* **Time Complexity:** `O(n × m)`
* **Space Complexity:** `O(n)`

Since `n, m ≤ 100`, the solution easily satisfies the given constraints.

---

## Key Concept

> A student is successful if they are among the students with the maximum score in **at least one subject**.

The important part is using a `set` so that each student is counted only once.

---

## Constraints

* `1 ≤ n, m ≤ 100`
* Each mark is between `1` and `9`
* Marks in each row are provided without spaces.

---

## Language

* **Python 3**
