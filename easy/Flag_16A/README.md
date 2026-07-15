# A. Flag

## 📌 Problem Overview
Berland wants to verify whether its flag follows the new ISO standard.

A valid flag must satisfy:
1. Every row consists of only one color (all characters in a row are identical).
2. Adjacent rows must have different colors.

Your task is to determine whether the given flag is valid.

---

## 💡 Approach

1. Read the flag.
2. For each row:
   - Verify every character matches the first character of that row.
3. Compare the first character of each row with the previous row.
   - If they are the same, the flag is invalid.
4. If all checks pass, print **YES**; otherwise print **NO**.

---

## ✅ Algorithm

1. Input `n` and `m`.
2. Store the flag.
3. For every row:
   - Check uniformity.
   - Check difference from previous row.
4. Output the result.

---

## ⏱ Complexity Analysis

- **Time Complexity:** `O(n × m)`
- **Space Complexity:** `O(n × m)`

---

## 🛠 Technologies Used

- Python 3
- Basic Loops
- String Processing

---

## 📚 Concepts Practiced

- Matrix Traversal
- String Manipulation
- Simulation
- Implementation