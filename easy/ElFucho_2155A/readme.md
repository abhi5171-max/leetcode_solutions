# Codeforces - A. El fucho

**Platform:** Codeforces  
**Problem:** A. El fucho  
**Language:** Python 3  
**Topics:** Mathematics, Implementation

## Problem Statement

Juan and his friends organize a modified double-elimination football tournament.

Initially, all `n` teams belong to the winners' group.

The tournament has three stages:

1. Winners' group: Teams play matches, and losing teams move to the losers' group.
2. Losers' group: Teams play matches, and losing teams are eliminated.
3. Final: The remaining team from each group plays one final match.

Find the total number of matches played in the tournament.

## Approach: Mathematical Observation

Instead of simulating every round, we can calculate the total number of matches directly.

### 1. Winners' Group

Initially, there are `n` teams.

Each match eliminates one team from the winners' group by moving it to the losers' group.

To leave one team in the winners' group:

`Winners' matches = n - 1`

### 2. Losers' Group

The `n - 1` teams that lost in the winners' group enter the losers' group.

To leave one team in this group:

`Losers' matches = n - 2`

### 3. Final Match

The two remaining teams play one final match.

`Final matches = 1`

### Final Formula

Adding all matches:

`Answer = (n - 1) + (n - 2) + 1`

Therefore:

`Answer = 2 * n - 2`

## Python 3 Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    print(2 * n - 2)
```

## Example

**Input:**

```text
2
2
3
```

**Output:**

```text
2
4
```

### Explanation

- Test Case 1: `n = 2`

  Total matches = `2 * 2 - 2 = 2`

- Test Case 2: `n = 3`

  Total matches = `2 * 3 - 2 = 4`

## Complexity Analysis

- **Time Complexity:** `O(1)` per test case because only a mathematical formula is evaluated.
- **Space Complexity:** `O(1)` because no additional data structures are required.

## Key Learnings

- Identifying mathematical patterns in tournament problems.
- Avoiding unnecessary simulation.
- Breaking a complex process into independent stages.
- Using direct formulas for optimal solutions.

---

**Final Formula:**

`Total Matches = 2 * n - 2`