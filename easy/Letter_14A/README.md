# A. Letter

## 📌 Problem Overview

Bob has drawn several shaded (`*`) squares on a rectangular sheet.

He wants to cut the **smallest possible rectangle** that contains every shaded square, minimizing mailing cost.

The task is to print that minimum bounding rectangle.

---

## 💡 Approach

The solution finds the outer boundaries of all shaded cells.

We maintain:

- Topmost row
- Bottommost row
- Leftmost column
- Rightmost column

After scanning the entire grid, simply print the rectangle enclosed by these boundaries.

---

## ✅ Algorithm

1. Read the grid.
2. Traverse every cell.
3. Whenever a `*` is found:
   - Update top boundary.
   - Update bottom boundary.
   - Update left boundary.
   - Update right boundary.
4. Print the submatrix inside these boundaries.

---

## ⏱ Complexity Analysis

- **Time Complexity:** `O(n × m)`
- **Space Complexity:** `O(n × m)`

---

## 🛠 Technologies Used

- Python 3
- Matrix Traversal
- Boundary Tracking

---

## 📚 Concepts Practiced

- 2D Arrays
- Bounding Rectangle
- Matrix Processing
- Implementation
```