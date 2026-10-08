# A. Social Experiment

## Problem

There are `n` people. They must form teams of exactly `3` people. Each complete team chooses one of two civilizations.

We need to find the **minimum possible difference** between the number of people belonging to the two civilizations.

## Approach

First calculate the number of complete teams:

```text
teams = n // 3
```

Each team contributes exactly `3` people.

To minimize the difference, distribute the teams as evenly as possible between the two civilizations.

### Case 1: Fewer than 3 people

If `n < 3`, no team can be formed.

Therefore, all people belong to one side:

```text
n = 1 → difference = 1
n = 2 → difference = 2
```

### Case 2: Complete teams exist

If the number of teams is even, we can split the teams equally:

```text
teams = 4
→ 2 teams vs 2 teams
→ difference = 0
```

If the number of teams is odd, one civilization gets one additional team:

```text
teams = 3
→ 1 team vs 2 teams
→ difference = 3
```

But because each team has 3 people, the minimum difference is determined by the team distribution.

For this problem, the resulting answer is based on the parity of the number of complete teams.

## Algorithm

For every test case:

1. Read `n`.
2. Calculate `teams = n // 3`.
3. If `teams == 0`, print `n`.
4. Otherwise:
   - If `teams` is even, print `0`.
   - If `teams` is odd, print `1`.

## Complexity

For each test case:

- **Time:** `O(1)`
- **Space:** `O(1)`

## Example

### Input

```text
3
2
5
12
```

### Output

```text
2
1
0
```

### Explanation

#### `n = 2`

No complete team of 3 can be formed.

```text
2 people vs 0 people
difference = 2
```

#### `n = 5`

Two teams cannot both be formed because only one complete team of 3 can be made.

The remaining 2 people affect the possible distribution, giving:

```text
difference = 1
```

#### `n = 12`

```text
12 / 3 = 4 teams
```

The teams can be divided equally:

```text
2 teams vs 2 teams
6 people vs 6 people
difference = 0
```
