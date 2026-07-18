# A. Towers

## Problem
Given `N` wooden bars, each with a known length, bars of the **same length** can be stacked together to form a tower.

Determine:
1. The height of the tallest tower.
2. The minimum number of towers needed.

## Approach
- Count the frequency of each bar length using a dictionary.
- The maximum frequency represents the tallest tower.
- The number of distinct bar lengths represents the total number of towers.

## Algorithm
1. Read `N` and the list of bar lengths.
2. Count the frequency of each length.
3. Find the maximum frequency.
4. Count the number of distinct lengths.
5. Output both values.

## Complexity
- **Time Complexity:** `O(N)`
- **Space Complexity:** `O(N)`

## Example

### Input
```
4
6 5 6 7
```

### Output
```
2 3
```

## Key Concepts
- Hash Map (Dictionary)
- Frequency Counting
- Greedy Observation