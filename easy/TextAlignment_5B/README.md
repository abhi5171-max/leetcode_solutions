# B. Center Alignment

## 📌 Problem Overview
Given multiple lines of text, format them inside the smallest possible rectangular frame made of `*` characters while **centering each line**.

If a line cannot be perfectly centered because the remaining spaces are odd, alternate the extra space between the right and left sides, starting with the **right side** (bringing the text closer to the left).

---

## 🧠 Approach

1. Read all input lines until EOF.
2. Determine the maximum line length.
3. Print the top border consisting of `*`.
4. For each line:
   - Calculate the number of extra spaces required.
   - If the spaces are even, split them equally.
   - If odd, alternate where the extra space is placed.
5. Print the formatted line enclosed by `*`.
6. Print the bottom border.

---

## ✅ Algorithm

1. Store all input lines.
2. Find the maximum width among all lines.
3. Print the top border.
4. For each line:
   - Compute padding.
   - Distribute spaces equally.
   - Alternate the extra space when padding is odd.
   - Print:
     ```
     *<left spaces><text><right spaces>*
     ```
5. Print the bottom border.

---

## ⏱ Complexity Analysis

- **Time Complexity:** `O(N)`
- **Space Complexity:** `O(N)`

where **N** is the total number of characters in the input.

---

## 💡 Key Concepts

- String formatting
- Padding
- Simulation
- Input until EOF
- Greedy implementation

---

## 🏷 Tags

`Implementation` `Strings` `Simulation`