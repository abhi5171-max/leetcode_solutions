Maximum Subarray
Problem Statement

Given an integer array nums, find the contiguous subarray with the largest sum and return its sum.

Example

Input

nums = [-2,1,-3,4,-1,2,1,-5,4]

Output

6

Explanation

The subarray [4,-1,2,1] has the largest sum.
Approach

This problem is solved using Kadane's Algorithm.

Traverse the array once.
At each element, decide whether to:
Start a new subarray from the current element.
Extend the previous subarray.
Keep track of the maximum subarray sum found so far.
Algorithm
Initialize current_sum and max_sum with the first element.
Iterate through the remaining elements.
Update:
current_sum = max(current element, current_sum + current element)
max_sum = max(max_sum, current_sum)
Return max_sum.
Python Solution
class Solution:
    def maxSubArray(self, nums):
        current_sum = max_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum
Complexity Analysis
Time Complexity: O(n)
Space Complexity: O(1)
Key Learning
Kadane's Algorithm
Dynamic Programming Optimization
Greedy Decision Making
Efficient Array Traversal