# B. New Year Cake 🎂

## Problem Description

Monocarp wants to bake a cake consisting of one or more layers. The top layer has size `1`, and each layer below it is twice the size of the layer directly above it.

Each layer must be covered with either white or dark chocolate, and the chocolate colors must alternate between consecutive layers.

Given `a` kilograms of white chocolate and `b` kilograms of dark chocolate, determine the maximum number of layers Monocarp can make without exceeding either chocolate supply.

## Approach

Use a greedy approach to test both possible starting colors:

1. White chocolate on the top layer.
2. Dark chocolate on the top layer.

For each possibility:

- Start with layer size `1`.

- Alternate the chocolate color for each consecutive layer.
- Double the layer size after every successful layer.
- Stop when the required chocolate exceeds the available supply.
- Return the maximum number of layers obtained from both attempts.

## Python Solution

```python
t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    white = dark = 0
    layers = 0
    size = 1

    while True:
        if layers % 2 == 0:
            white += size
        else:
            dark += size

        if white > a or dark > b:
            break

        layers += 1
        size *= 2

    white = dark = 0
    layers2 = 0
    size = 1

    while True:
        if layers2 % 2 == 0:
            dark += size
        else:
            white += size

        if white > a or dark > b:
            break

        layers2 += 1
        size *= 2

    print(max(layers, layers2))
```

## Example

**Input

```text
7
1 1
1 2
3 1
4 3
5 2
1000000 1000000
1000000 1
```

**Output

```text
1
2
2
2
3
20
2
```

## Complexity Analysis

- **Time Complexity:** `O(log(max(a, b)))` per test case.
- **Space Complexity:** `O(1)` auxiliary space.

## Key Learning

This problem demonstrates greedy simulation, alternating conditions, and handling exponentially increasing values while respecting resource constraints.

## Tags

`Codeforces` `Greedy` `Implementation` `Math` `Python`
