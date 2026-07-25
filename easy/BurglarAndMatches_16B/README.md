# B. Burglar and Matches

## Problem Statement
A burglar has a backpack that can carry exactly **n matchboxes**.

There are **m containers**, where:
- `a_i` = number of matchboxes in the container
- `b_i` = matches inside each matchbox

Find the maximum number of matches the burglar can steal.

## Approach
This is a classic **Greedy Algorithm** problem.

To maximize the total matches:
- Always pick matchboxes from the container having the **highest number of matches per box** first.
- Continue until the backpack becomes full.

Since every matchbox occupies the same amount of space, choosing boxes with the highest value first always produces the optimal answer.

## Algorithm
1. Read all containers.
2. Store each as `(matches_per_box, number_of_boxes)`.
3. Sort the containers in descending order of matches per box.
4. For each container:
   - Take as many boxes as possible.
   - Add their matches to the answer.
   - Reduce the remaining backpack capacity.
5. Stop when the backpack is full.

## Correctness
The greedy choice is optimal because:
- Every box has identical size.
- The only factor affecting the answer is the number of matches inside each box.
- Taking higher-value boxes before lower-value ones can never reduce the total number of matches.

Therefore, the algorithm always computes the maximum possible number of matches.

## Complexity Analysis
- **Time Complexity:** `O(m log m)` (sorting)
- **Space Complexity:** `O(m)`

## Concepts Used
- Greedy Algorithm
- Sorting
- Simulation
- Optimization
```