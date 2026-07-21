# A. Codecraft III

## Problem Overview
Given the current month and the number of months remaining until the release of Codecraft III, determine the month in which it will be released.

## Approach
- Store all 12 months in a list in chronological order.
- Find the index of the current month.
- Add `k` months to the current index.
- Use modulo (`% 12`) to wrap around the calendar.
- Print the resulting month.

## Algorithm
1. Store all months in a list.
2. Read the current month and integer `k`.
3. Find the current month's index.
4. Compute:
   ```
   new_index = (current_index + k) % 12
   ```
5. Print the month at `new_index`.

## Complexity Analysis
- **Time Complexity:** `O(1)`
- **Space Complexity:** `O(1)`

## Key Concepts
- Arrays (Lists)
- Indexing
- Modulo Arithmetic
- Simulation