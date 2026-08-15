B. Fortune Telling — README
Problem

Marina has n camomile flowers. Each flower has a certain number of petals.

She can choose one or more flowers to form a bouquet. She then tears off all the petals one by one.

The fortune-telling result alternates:

Loves
Doesn't love
Loves
Doesn't love
...

Since Marina always starts with "Loves", the final result is "Loves" exactly when the total number of petals is odd.

The task is to find the maximum possible total number of petals that is odd.

If no bouquet with an odd number of petals exists, print 0.

Key Idea

We only care about whether the total number of petals is odd or even.

Case 1: Total sum is already odd

If we take all flowers, the total is odd.

Therefore, the answer is simply:

sum(a)
Case 2: Total sum is even

We need to remove the smallest possible number of petals to make the sum odd.

To change an even sum into an odd sum, we must remove an odd number.

The smallest possible odd number to remove is the smallest odd-valued flower.

So:

answer = total_sum - smallest_odd

If there is no odd-valued flower, every flower has an even number of petals, so every possible bouquet has an even number of petals. The answer is 0.