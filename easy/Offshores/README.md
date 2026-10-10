# B. Offshores

## 📌 Problem Overview

**Problem:** B. Offshores  
**Platform:** Codeforces  
**Topic:** Greedy, Arrays, Mathematics

Given `n` banks with initial balances `a[i]`, each transfer removes `x` rubles from one bank and credits `y` rubles to another bank, where `y <= x`.

The goal is to maximize the amount of money that can end up in a single bank.

## 🧠 Approach

For each bank, calculate how many complete transfers it can make: `a[i] // x`.

Each transfer contributes `y` rubles to the destination bank. The optimal destination is the bank with the maximum value of:

`a[i] - (a[i] // x) * y`

This accounts for the balance retained by choosing that bank as the destination instead of using it as a source.

## ✅ Algorithm

1. Read the number of test cases.
2. For each test case, read `n`, `x`, `y`, and the array `a`.
3. Calculate the total contribution from all banks: `sum((v // x) * y for v in a)`.
4. Find the maximum value of `v - (v // x) * y`.
5. Add these two values and print the result.

## ⏱ Complexity Analysis

- **Time Complexity:** O(n) per test case.
- **Space Complexity:** O(n) for storing the array.

## 💡 Key Concepts

- Greedy optimization
- Integer division and modulo
- Array traversal
- Mathematical observation

## 🏷️ Tags

`Codeforces` `Python` `Greedy` `Arrays` `Math`
