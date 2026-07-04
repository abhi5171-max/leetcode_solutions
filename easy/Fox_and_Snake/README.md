# Fox And Snake

## Problem Statement

Draw a snake on an `n × m` grid using the following pattern:

* The snake starts from the top-left corner.
* Every even-numbered row (0-based indexing) is completely filled with `#`.
* The snake alternates between the right and left sides on the odd rows.

Empty cells are represented using `.`.

---

## Approach

The snake follows a repeating **4-row pattern**:

```text
Row 0 : ########
Row 1 : .......#
Row 2 : ########
Row 3 : #.......
```

This pattern repeats until all rows are printed.

For each row:

* If the row index is even:

  * Print `#` repeated `m` times.
* Otherwise:

  * Alternate between placing the snake on the right and left using:

```text
(i // 2) % 2
```

---

## Algorithm

1. Read `n` and `m`.
2. Iterate through each row:

   * If the row index is even:

     * Print `# * m`.
   * Otherwise:

     * If `(row // 2) % 2 == 0`:

       * Print dots followed by one `#`.
     * Else:

       * Print one `#` followed by dots.
3. Continue until all rows are printed.

---

## Correctness

* Every even row is fully occupied by the snake.
* Odd rows alternate between placing the snake on the right and left ends.
* The alternating condition creates the exact zig-zag path required by the problem.

---

## Complexity Analysis

* **Time Complexity:** `O(n × m)`
* **Space Complexity:** `O(1)` (excluding output)

---

## Python Solution

```python
n, m = map(int, input().split())

for i in range(n):
    if i % 2 == 0:
        print("#" * m)
    elif (i // 2) % 2 == 0:
        print("." * (m - 1) + "#")
    else:
        print("#" + "." * (m - 1))
```

---

## Key Concepts

* Pattern Printing
* Loops
* Conditional Statements
* Grid Simulation
* Modulo Arithmetic
