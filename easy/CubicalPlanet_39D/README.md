# D. Cubical Planet

## Problem

Two flies are sitting on different vertices of a cube. Determine whether they can see each other. Two vertices are visible to each other if they lie on the **same face** of the cube.

## Approach

* Read the coordinates of both vertices.
* Check whether they share at least one coordinate (`x`, `y`, or `z`).
* If at least one coordinate is the same, they are on a common face, so print `YES`.
* Otherwise, print `NO`.

## Algorithm

1. Read the coordinates of the first vertex.
2. Read the coordinates of the second vertex.
3. Compare corresponding coordinates:

   * If `x`, `y`, or `z` matches, print `YES`.
   * Otherwise, print `NO`.

## Complexity

* **Time Complexity:** `O(1)`
* **Space Complexity:** `O(1)`

## Python Solution

```python
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if a[0] == b[0] or a[1] == b[1] or a[2] == b[2]:
    print("YES")
else:
    print("NO")
```

## Example

**Input**

```
0 0 0
0 1 0
```

**Output**

```
YES
```

## Key Concepts

* Geometry
* Coordinate Comparison
* Conditional Statements
* Basic Implementation
