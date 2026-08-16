# A. Clothes

## Problem

Gerald wants to buy **three clothing items that all match each other**.

There are:

* `n` clothing items
* `m` matching pairs
* `ai` = price of the `i`-th clothing item

A matching pair `(u, v)` means clothing item `u` matches clothing item `v`.

We need to find the **minimum total price of three mutually matching items**.

If no such group of three exists, print `-1`.

---

## Key Idea

We can represent the clothing items as a **graph**:

* Each clothing item is a vertex.
* Each matching pair is an edge.

We need to find a group of **three vertices where every pair is connected**.

This is called a **triangle** in graph theory.

For every clothing item `i`, we can check all pairs of its neighbors.

Suppose `j` and `k` are both connected to `i`.

If `j` and `k` are also connected, then:

```text
i, j, k
```

form a triangle.

The cost of buying them is:

```text
a[i] + a[j] + a[k]
```

We keep the minimum such cost.

---

## Important Observation

For a triangle involving vertices `i`, `j`, and `k`, when we process vertex `i`, the other two vertices must both be neighbors of `i`.

Therefore, for every vertex:

1. Look at all its neighbors.
2. Check every pair of neighbors.
3. Determine whether those two neighbors are also connected.
4. If yes, we found a matching group of three.

Because `n` is small enough for this approach, checking neighbor pairs is sufficient.

---

## Python 3 Solution

```python
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

price = list(map(int, input().split()))

graph = [[] for _ in range(n)]
connected = [[False] * n for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1

    graph[u].append(v)
    graph[v].append(u)

    connected[u][v] = True
    connected[v][u] = True


INF = float('inf')
answer = INF

for i in range(n):
    neighbors = graph[i]

    # Check every pair of neighbors of i
    for x in range(len(neighbors)):
        j = neighbors[x]

        for y in range(x + 1, len(neighbors)):
            k = neighbors[y]

            # j and k must also match
            if connected[j][k]:
                total = price[i] + price[j] + price[k]
                answer = min(answer, total)

if answer == INF:
    print(-1)
else:
    print(answer)
```

---

## Example 1

### Input

```text
3 3
1 2 3
1 2
2 3
3 1
```

The graph is:

```text
1 ----- 2
 \       /
  \     /
    3
```

All three items match each other.

Their total price is:

```text
1 + 2 + 3 = 6
```

### Output

```text
6
```

---

## Example 2

### Input

```text
3 2
2 3 4
2 3
2 1
```

The matching pairs are:

```text
1 -- 2 -- 3
```

Items `1` and `3` do not match.

Therefore, there is no group of three mutually matching items.

### Output

```text
-1
```

---

## Example 3

### Input

```text
4 4
1 1 1 1
1 2
2 3
3 4
4 1
```

The graph forms a cycle:

```text
1 -- 2
|    |
4 -- 3
```

There is no triangle because no three vertices are mutually connected.

Therefore:

```text
-1
```

---

## Complexity

For each vertex, we check pairs of its neighbors.

The complexity is:

```text
O(Σ degree(v)²)
```

In the worst case, this is:

```text
O(n³)
```

The adjacency matrix requires:

```text
O(n²)
```

memory.

With the given constraints, this is easily fast enough.

---

## Key Takeaway

The problem is simply a **minimum-weight triangle detection** problem.

We need three clothing items such that:

```text
1 matches 2
2 matches 3
3 matches 1
```

For every such triangle, calculate:

```text
price[1] + price[2] + price[3]
```

and take the minimum.

If no triangle exists, print `-1`.

## Tags

* Codeforces
* Graph Theory
* Triangle Detection
* Adjacency Matrix
* Adjacency List
* Implementation
* Python 3
