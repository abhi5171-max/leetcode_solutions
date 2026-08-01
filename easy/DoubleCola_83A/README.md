# A. Double Cola

## 📌 Problem

Five friends—**Sheldon, Leonard, Penny, Rajesh, and Howard**—stand in a queue to buy cans of Double Cola. After drinking a can, the person is duplicated, and both copies move to the end of the queue. Given the number `n`, determine who drinks the `n`-th can.

## 💡 Approach

Instead of simulating the queue (which becomes extremely large), observe that:

* Initially, each person appears **once**.
* After each complete round, the number of copies of every person doubles.
* Each round contains `5 × group_size` drinks, where `group_size` is the current number of copies for each person.

Algorithm:

1. Start with `group_size = 1`.
2. While `n` is greater than the current round size (`5 × group_size`):

   * Subtract the current round size from `n`.
   * Double `group_size`.
3. The answer is determined by `(n - 1) // group_size`.

## ✅ Complexity

* **Time:** `O(log n)`
* **Space:** `O(1)`

## 🛠️ Topics

* Math
* Simulation
* Implementation
* Binary Growth

## 📚 Key Learning

* Avoid direct simulation when values grow exponentially.
* Recognize repeating patterns and process them in groups for efficiency.
