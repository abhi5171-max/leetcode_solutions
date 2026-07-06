Merge Intervals
Problem Statement

Given an array of intervals, merge all overlapping intervals and return an array of the non-overlapping intervals.

Example

Input

intervals = [[1,3],[2,6],[8,10],[15,18]]

Output

[[1,6],[8,10],[15,18]]
Approach

The solution uses Sorting + Greedy.

Sort intervals based on their starting point.
Traverse the sorted intervals.
If the current interval overlaps with the last merged interval, merge them.
Otherwise, add it as a new interval.
Algorithm
Sort intervals by start time.
Initialize an empty result list.
For each interval:
If there is no overlap, append it.
Otherwise, merge by updating the ending value.
Return the merged intervals.
Python Solution
class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])

        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
Complexity Analysis
Time Complexity: O(n log n)
Sorting: O(n log n)
Traversal: O(n)
Space Complexity: O(n)
Key Learning
Sorting Intervals
Greedy Algorithms
Interval Merging
Edge Case Handling
Efficient List Manipulation