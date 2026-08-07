# 📸 Young Photographer

## Problem
Bob is standing at position `x0` on a straight racetrack. Each athlete runs only within a specific segment of the track. Bob can photograph an athlete only if he stands somewhere inside that athlete's segment.

Find the minimum distance Bob must move so that there exists a single position from which he can photograph every athlete. If no such position exists, output `-1`.

## Approach
- Convert every segment into the form `[min(ai, bi), max(ai, bi)]`.
- Compute the intersection of all segments:
  - `left = maximum of all left endpoints`
  - `right = minimum of all right endpoints`
- If `left > right`, no common position exists, so print `-1`.
- Otherwise:
  - If `x0` lies inside the intersection, answer is `0`.
  - If `x0` is left of the intersection, move to `left`.
  - If `x0` is right of the intersection, move to `right`.

## Algorithm
1. Read input.
2. Normalize every segment.
3. Find the common intersection.
4. Check if the intersection exists.
5. Compute the minimum movement.

## Complexity
- **Time:** `O(n)`
- **Space:** `O(1)`

## Concepts Used
- Interval Intersection
- Greedy
- Simulation