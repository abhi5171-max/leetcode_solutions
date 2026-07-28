# A. Spit Problem

## Problem Overview
Bob observed camels in a zoo and recorded each camel's position and the direction and distance of its spit. A camel at position `x` spitting a distance `d` can only hit a camel located at `x + d`.

The task is to determine whether there exists a pair of camels that spit at each other.

## Approach
- Store each camel's position and spit distance in a dictionary.
- For every camel:
  - Compute the target position `x + d`.
  - Check if another camel exists at that position.
  - Verify whether the second camel spits back to the first.
- If such a pair is found, print **YES**; otherwise, print **NO**.

## Algorithm
1. Read all camel positions and spit distances.
2. Store them in a dictionary:
   - Key → Position
   - Value → Spit distance
3. For each camel:
   - Find the target position.
   - If a camel exists there and its spit returns to the current camel, output **YES**.
4. If no valid pair exists, output **NO**.

## Correctness
The algorithm explicitly checks every camel's spit target and verifies the reverse spit condition. Therefore, every possible pair that could spit at each other is examined exactly once.

## Complexity Analysis
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

## Python Solution

```python
n = int(input())

camels = {}

for _ in range(n):
    x, d = map(int, input().split())
    camels[x] = d

for x, d in camels.items():
    target = x + d
    if target in camels and target + camels[target] == x:
        print("YES")
        break
else:
    print("NO")
```

## Key Concepts
- Dictionary (Hash Map)
- Simulation
- Constant-time lookup