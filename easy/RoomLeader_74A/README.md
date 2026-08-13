# A. Room Leader

## Problem

In a Codeforces room, each contestant receives points from five problems: `A`, `B`, `C`, `D`, and `E`.

Contestants can also perform hacks:

* Each successful hack gives **+100 points**.
* Each unsuccessful hack gives **−50 points**.

The task is to find the contestant with the highest total score.

## Score Calculation

For each contestant:

```text id="8u1y9f"
Total Score =
    A + B + C + D + E
    + (successful hacks × 100)
    - (unsuccessful hacks × 50)
```

A problem that was not solved contributes `0` points.

## Approach

1. Read the number of contestants `n`.
2. For each contestant:

   * Read their handle.
   * Read successful and unsuccessful hack counts.
   * Read points for problems `A` through `E`.
3. Calculate the contestant's total score.
4. Keep track of the contestant with the maximum score.
5. Print the handle of the leader.

The problem guarantees that there is exactly one contestant with the maximum score.

## Example

### Input

```text id="8qz2xu"
5
Petr 3 1 490 920 1000 1200 0
tourist 2 0 490 950 1100 1400 0
Egor 7 0 480 900 950 0 1000
c00lH4x0R 0 10 150 0 0 0 0
some_participant 2 1 450 720 900 0 0
```

### Scores

```text id="6v8f3j"
Petr             → 3860
tourist           → 4140
Egor              → 4030
c00lH4x0R         → -350
some_participant  → 2220
```

The highest score is `4140`, achieved by `tourist`.

### Output

```text id="4f9s4k"
tourist
```

## Complexity

For `n` contestants, each contestant has a fixed number of values to process.

* **Time:** `O(n)`
* **Space:** `O(1)` extra space

## Language

* Python 3

## Key Concepts

* Input parsing
* Arithmetic operations
* Maximum value tracking
* Iteration
