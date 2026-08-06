# B. T-shirts from Sponsor

## Problem
Given the available quantity of T-shirts in five sizes (`S`, `M`, `L`, `XL`, `XXL`) and a queue of participants with preferred sizes, assign each participant a T-shirt.

If the preferred size is unavailable, the participant chooses the closest available size. If two sizes are equally close, the larger size is preferred.

## Approach
- Store the available quantity of each T-shirt size.
- Represent the sizes in order:
  ```
  S → M → L → XL → XXL
  ```
- For each participant:
  - Find the index of the preferred size.
  - Check all available sizes.
  - Choose the size with:
    - Minimum distance from the preferred size.
    - If distances are equal, choose the larger size.
  - Print the assigned size and decrease its count.

## Algorithm
1. Read the number of T-shirts for each size.
2. Store the sizes in an ordered list.
3. For every participant:
   - Determine the preferred size index.
   - Search all available sizes.
   - Select the closest size (larger one in case of a tie).
   - Output the assigned size and update the inventory.

## Complexity
- **Time:** O(K)
- **Space:** O(1)

## Concepts Used
- Arrays
- Greedy Simulation
- String Processing