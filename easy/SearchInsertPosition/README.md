Here’s a clean README you can use for the solution:

# Search Insert Position

## Problem

Given a sorted array of distinct integers and a target value, return the index if the target is found.

If the target is not found, return the index where it would be inserted to maintain the sorted order.

The solution must have **O(log n)** runtime complexity.

## Examples

### Example 1

```text
Input:  nums = [1,3,5,6], target = 5
Output: 2
```

### Example 2

```text
Input:  nums = [1,3,5,6], target = 2
Output: 1
```

### Example 3

```text
Input:  nums = [1,3,5,6], target = 7
Output: 4
```

## Approach

Because the array is already sorted, we can use **Binary Search**.

1. Set `left` to the first index and `right` to the last index.
2. Calculate the middle index.
3. If `nums[mid]` equals `target`, return `mid`.
4. If `nums[mid]` is smaller than `target`, search the right half.
5. Otherwise, search the left half.
6. When the loop ends, `left` represents the correct insertion position.

## Python 3 Solution

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left
```

## Complexity Analysis

* **Time Complexity:** `O(log n)`
* **Space Complexity:** `O(1)`

## Key Insight

When binary search finishes without finding the target, `left` is positioned exactly where the target should be inserted while keeping the array sorted.

## Constraints

* `1 <= nums.length <= 10^4`
* `-10^4 <= nums[i] <= 10^4`
* `nums` contains distinct values sorted in ascending order.
* `-10^4 <= target <= 10^4`

## Topic

**Binary Search**
