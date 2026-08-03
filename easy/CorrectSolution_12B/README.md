# B. Correct Solution?

## 📌 Problem
Alice gives Bob a number **n** and asks him to rearrange its digits to form the **smallest possible number without leading zeros**.

Bob provides an answer **m**. The task is to determine whether Bob's answer is correct.

---

## 💡 Approach

1. Read the original number `n` and Bob's answer `m`.
2. Verify that both numbers contain exactly the same digits.
3. Sort the digits of `n`.
4. Construct the smallest possible number:
   - Place the smallest non-zero digit first.
   - Append all remaining digits (including zeros) in ascending order.
5. Compare the constructed number with `m`.
6. Print:
   - `OK` if they match.
   - `WRONG_ANSWER` otherwise.

---

## ✅ Algorithm

1. Sort the digits of `n`.
2. Find the first non-zero digit.
3. Move it to the front.
4. Append the remaining sorted digits.
5. Compare with Bob's answer.

---

## ⏱ Complexity Analysis

- **Time Complexity:** `O(d log d)`
- **Space Complexity:** `O(d)`

where `d` is the number of digits (maximum 10).

---

## 🛠 Technologies Used

- Python 3

---

## 📚 Concepts Used

- Sorting
- String Manipulation
- Greedy Construction

---

## 🚀 Outcome

Efficiently verifies whether Bob produced the smallest possible rearrangement of the given number while avoiding leading zeros.