# A. Chips

## Problem

The presenter has **m** chips and **n** walruses sitting in a circle. Starting from walrus `1`, the presenter gives `i` chips to walrus `i`, where `i` is the walrus's number. After walrus `n`, the process repeats from walrus `1`.

If the presenter does not have enough chips to give the required amount, the process stops. The task is to determine how many chips remain.

## Approach

* Start with walrus `1`.
* Continue distributing chips while enough chips are available.
* After reaching walrus `n`, wrap back to walrus `1`.
* Stop when the remaining chips are fewer than the required amount.
* Output the remaining chips.

## Algorithm

1. Read `n` and `m`.
2. Initialize the current walrus number to `1`.
3. While `m >= current_walrus_number`:

   * Subtract the required chips from `m`.
   * Move to the next walrus.
   * If the current walrus exceeds `n`, reset it to `1`.
4. Print the remaining chips.

## Complexity Analysis

* **Time Complexity:** `O(k)`, where `k` is the number of successful chip distributions (at most around `10,000` because `m ≤ 10⁴`).
* **Space Complexity:** `O(1)`.

## Key Concepts

* Simulation
* Circular Traversal
* Loops
