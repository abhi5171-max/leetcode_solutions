# B. Flipping Binary String

## 📌 Problem Overview

**Problem:** B. Flipping Binary String  
**Platform:** Codeforces  
**Topic:** Binary Strings, Parity, Greedy

Given a binary string `s` of length `n`, an operation selects an index `i` and flips every bit except the bit at that index.

Each index can be selected at most once. The goal is to make every bit zero or report `-1` if it is impossible.

## 🧠 Approach

Let:

- `ones` contain the indices where the string has bit `1`.
- `zeros` contain the indices where the string has bit `0`.

There are two possible valid constructions:

1. **Even number of ones:** Select all indices containing `1`.
2. **Odd number of zeros:** Select all indices containing `0`.

If neither condition holds, output `-1`.

The solution follows from the parity of the number of operations affecting each bit.

## ✅ Algorithm

1. Read the number of test cases.
2. For each test case, read `n` and the binary string `s`.
3. Collect the 1-based indices of all `1`s and `0`s.
4. If the number of ones is even, print their count and indices.
5. Otherwise, if the number of zeros is odd, print their count and indices.
6. If neither condition holds, print `-1`.

## ⏱ Complexity Analysis

- **Time Complexity:** O(n) per test case.
- **Space Complexity:** O(n) for storing the selected indices.

## 💡 Key Concepts

- Binary strings
- Bit flipping
- Parity
- Greedy construction
- Index manipulation

## 🏷️ Tags

`Codeforces` `Python` `Binary String` `Greedy` `Parity` `Implementation`
