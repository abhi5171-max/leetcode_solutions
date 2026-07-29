# A. Train and Peter

## 📌 Problem Overview

Peter remembers two sequences of station flag colors that he saw during two separate periods of wakefulness on a train journey.

Determine whether these two sequences can appear:

- only while traveling from **A → B** (`forward`)
- only while traveling from **B → A** (`backward`)
- in **both** directions (`both`)
- in **neither** direction (`fantasy`)

The second sequence must appear **after** the first one without reusing characters.

---

## 🧠 Approach

We check both directions independently.

### Forward
1. Find the first occurrence of the first string.
2. Search for the second string starting after the end of the first.
3. If both are found, forward is possible.

### Backward
Repeat the same process on the reversed main string.

Finally:
- Both true → `both`
- Only forward → `forward`
- Only backward → `backward`
- Neither → `fantasy`

---

## ✅ Algorithm

1. Read the three strings.
2. Define a helper function:
   - Find first substring.
   - Search for the second substring after it.
3. Run the function on:
   - Original string.
   - Reversed string.
4. Print the appropriate answer.

---

## ⏱ Complexity Analysis

- **Time Complexity:** `O(N)`
- **Space Complexity:** `O(N)`

where **N** is the length of the main string.

---

## 💡 Key Concepts

- String searching
- `find()` function
- Greedy matching
- String reversal
- Simulation

---

## 🏷 Tags

`Strings` `Implementation` `Greedy`