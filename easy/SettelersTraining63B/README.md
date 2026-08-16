B. Settlers' Training — README
Problem

You have n soldiers, each with a rank from 1 to k.

During one training session:

Soldiers are grouped by their current rank.
From every group whose rank is less than k, exactly one soldier increases their rank by 1.
One training session costs 1 golden coin.

The goal is to determine the minimum number of training sessions required to make all soldiers rank k.

Constraints
1 ≤ n, k ≤ 100
The ranks are given in non-decreasing order.
Key Idea

We can simulate the training process.

For each training session:

Find every distinct rank below k.
Increase one soldier from each such rank by 1.
Repeat until every soldier reaches rank k.

Because the input is small (n, k ≤ 100), direct simulation is simple and fast.

For example:

4 4
1 2 2 3

The process is:

1 2 2 3
↓
2 2 3 4
↓
2 3 4 4
↓
3 4 4 4
↓
4 4 4 4

Therefore, the answer is 4.