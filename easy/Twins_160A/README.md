Approach

To minimize the number of coins while ensuring your sum is strictly greater than the sum of the remaining coins:

Compute the total sum of all coins.
Sort the coins in descending order.
Pick the largest coins one by one until the sum of the picked coins becomes greater than the sum of the remaining coins (picked_sum > total_sum - picked_sum).
The number of picked coins is the answer.

This greedy approach works because taking larger coins first minimizes the number of coins needed.

Python 3 Solution
n = int(input())
coins = list(map(int, input().split()))

coins.sort(reverse=True)

total_sum = sum(coins)
picked_sum = 0
count = 0

for coin in coins:
    picked_sum += coin
    count += 1
    if picked_sum > total_sum - picked_sum:
        break

print(count)
Example

Input:

3
2 1 2

Sorted coins: [2, 2, 1]

Pick 2: picked sum = 2, remaining sum = 3 (not enough)
Pick another 2: picked sum = 4, remaining sum = 1 (4 > 1)

Output:

2
Complexity Analysis
Sorting: O(n log n)
Traversing the array: O(n)
Overall: O(n log n)
Space complexity: O(1) (excluding the input array)