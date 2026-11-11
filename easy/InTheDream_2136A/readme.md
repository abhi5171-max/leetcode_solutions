# A. In the Dream

**Platform:** Codeforces  
**Problem:** [A. In the Dream](https://codeforces.com/problemset/problem/2133/A)  
**Language:** Python 3  
**Topics:** Mathematics, Greedy, Implementation

## Problem Summary

Two football teams, RiOI and KDOI, play a match consisting of two halves.

The scores are:
- First half: `a:b`
- Final score: `c:d`

Neither team can score three consecutive goals in the same half.

Determine whether the given scores are possible.

## Approach: Mathematical Observation

For a half in which the two teams score `x` and `y` goals, a valid sequence exists if:

\[
\max(x,y) \leq 2(\min(x,y)+1)
\]

### Explanation

The team with fewer goals creates gaps between its goals.

For example, if RiOI scores 2 goals and KDOI scores 5 goals, one possible sequence is:

`KKRKKRK`

The goals of either team never appear three times consecutively.

The maximum number of goals that one team can score without creating three consecutive goals is twice the number of goals scored by the other team plus two.

We must apply this condition independently to both halves.

### Step 1: Check the First Half

The first-half scores are:

- RiOI: `a`
- KDOI: `b`

Check:

\[
\max(a,b) \leq 2(\min(a,b)+1)
\]

### Step 2: Calculate the Second-Half Goals

The final score includes goals from both halves.

Therefore:

- RiOI's second-half goals = `c - a`
- KDOI's second-half goals = `d - b`

Check:

\[
\max(c-a,d-b) \leq 2(\min(c-a,d-b)+1)
\]

### Step 3: Determine the Answer

If both halves satisfy the condition, print `YES`.

Otherwise, print `NO`.

## Python 3 Solution

```python
t = int(input())

for _ in range(t):
    a, b, c, d = map(int, input().split())

    first_half = max(a, b) <= 2 * (min(a, b) + 1)

    r = c - a
    k = d - b

    second_half = max(r, k) <= 2 * (min(r, k) + 1)

    if first_half and second_half:
        print("YES")
    else:
        print("NO")
```

## Example Dry Run

**Input:**
```text
3
1 4 1 4
1 4 2 5
0 100 0 100
```

**Test Case 1:**

First half: `1:4`

\[
4 \leq 2(1+1) \quad \text{False}
\]

Correction: the actual condition is \(4 \leq 4\), which is **True**.

Second half: `0:0`

Both halves are valid.

Output: `YES`

**Test Case 2:**

First half: `1:4`

Valid.

Second half: `1:1`

Valid.

Output: `YES`

**Test Case 3:**

First half: `0:100`

\[
100 \leq 2(0+1)
\]

False.

Output: `NO`

**Output:**
```text
YES
YES
NO
```

## Complexity Analysis

| Complexity | Value | Explanation |
|---|---|---|
| Time | O(1) per test case | Only arithmetic and comparison operations |
| Space | O(1) | Uses a constant number of variables |

## Key Learnings

- Convert final scores into second-half scores using subtraction.
- Treat each half independently because consecutive-goal restrictions reset between halves.
- Use a mathematical condition instead of generating every possible goal sequence.
- A greedy mathematical observation can reduce a sequence-validation problem to constant time.

