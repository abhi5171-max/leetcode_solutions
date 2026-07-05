# Best Time to Buy and Sell Stock

## Problem Statement

You are given an array `prices` where `prices[i]` represents the price of a stock on the `i-th` day.

You want to maximize your profit by choosing:

* **One day to buy** the stock.
* **A later day to sell** the stock.

Return the maximum profit possible. If no profit can be made, return `0`.

### Example

**Input**

```text
prices = [7,1,5,3,6,4]
```

**Output**

```text
5
```

**Explanation**

* Buy at price **1**
* Sell at price **6**
* Profit = **6 - 1 = 5**

---

## Approach

The optimal solution uses a **single traversal** of the array.

* Keep track of the **minimum stock price** encountered so far.
* For each day's price:

  * Calculate the profit if the stock were sold on that day.
  * Update the maximum profit whenever a larger profit is found.

This eliminates the need to compare every pair of days.

---

## Algorithm

1. Initialize:

   * `min_price` as the first price.
   * `max_profit` as `0`.
2. Traverse the array.
3. Update the minimum price seen so far.
4. Calculate the current profit.
5. Update the maximum profit if needed.
6. Return the maximum profit.

---

## Complexity Analysis

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

---

## Key Concepts

* Array Traversal
* Greedy Approach
* Running Minimum
* Optimization
