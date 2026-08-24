# A. Rank List

## Problem Statement

You are given the final results of a programming contest. Each team has:

* `p` — number of problems solved
* `t` — total penalty time

Teams are ranked using the following rules:

* More solved problems means a better rank.
* If two teams solve the same number of problems, the team with lower penalty time ranks higher.
* Teams with the same `p` and `t` share the same places.

Given `k`, find how many teams share the **k-th place**.

---

## Approach

We can sort the teams according to the contest ranking rules:

1. `p` in **descending order**
2. `t` in **ascending order**

After sorting, the team at index `k - 1` is the team occupying the `k-th position`.

All teams having the same `(p, t)` as this team share the same rank range.

So, we simply count how many teams have the same `(p, t)`.

### Example

For:

```text
7 2
4 10
4 10
4 10
3 20
2 1
2 1
1 10
```

After sorting:

```text
4 10
4 10
4 10
3 20
2 1
2 1
1 10
```

The team at the 2nd position has:

```text
p = 4
t = 10
```

There are **3** teams with these exact results.

Therefore, the answer is `3`.

---

## Algorithm

1. Read `n` and `k`.
2. Store all teams as `(p, t)`.
3. Sort the teams by:

   * `p` descending
   * `t` ascending
4. Select `teams[k - 1]`.
5. Count how many teams have the same `(p, t)`.
6. Print the count.

---

## Python 3 Solution

```python
n, k = map(int, input().split())

teams = []

for _ in range(n):
    p, t = map(int, input().split())
    teams.append((p, t))

# Sort by:
# 1. Problems solved -> descending
# 2. Penalty time -> ascending
teams.sort(key=lambda x: (-x[0], x[1]))

# Get the team at the k-th position
target = teams[k - 1]

# Count teams with the same score
answer = teams.count(target)

print(answer)
```

---

## Complexity Analysis

* **Time Complexity:** `O(n log n)`
* **Space Complexity:** `O(n)`

Since `n ≤ 50`, the solution is easily within the given limits.

---

## Key Insight

The main idea is:

> **Find the performance corresponding to the k-th position after sorting, then count all teams with that exact performance.**

Teams with identical `(problems solved, penalty time)` are considered tied, so they all share the corresponding places.
