# C. Fruits

## 📌 Problem

Valera has a shopping list containing multiple fruits, where the same fruit may appear several times.

The fruit seller has not assigned price tags to fruit types yet. Given the available prices, determine:

- The **minimum** possible total cost.
- The **maximum** possible total cost.

---

## 💡 Approach

1. Count how many times each fruit appears.
2. Sort the fruit frequencies in descending order.
3. Sort the prices.
4. For the minimum cost:
   - Assign the cheapest prices to the most frequently purchased fruits.
5. For the maximum cost:
   - Assign the most expensive prices to the most frequently purchased fruits.
6. Output both totals.

---

## ✅ Algorithm

1. Read input.
2. Count fruit occurrences using a frequency map.
3. Sort frequencies in descending order.
4. Sort prices in ascending order.
5. Compute:
   - Minimum cost
   - Maximum cost
6. Print the results.

---

## ⏱ Complexity Analysis

- **Time Complexity:** `O(n log n + m log m)`
- **Space Complexity:** `O(n)`

where:

- `n` = number of fruit types
- `m` = number of fruits in Valera's list

---

## 🛠 Technologies Used

- Python 3

---

## 📚 Concepts Used

- Greedy Algorithm
- Sorting
- Hash Map (Counter)
- Frequency Counting

---

## 🚀 Outcome

Finds the smallest and largest possible shopping costs by optimally assigning prices to fruit types based on purchase frequency.