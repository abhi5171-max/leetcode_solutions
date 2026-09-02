Here’s a clean GitHub-ready README for the problem:

# Remove Duplicates from Sorted Array

## Problem

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates **in-place** so that each unique element appears only once.

The relative order of the elements must remain unchanged.

Return the number of unique elements `k`.

After removing duplicates:

* The first `k` elements of `nums` must contain all unique values.
* The values must remain in sorted order.
* Elements after index `k - 1` can be ignored.

## Examples

### Example 1

```text
Input:  nums = [1,1,2]
Output: 2
nums = [1,2,_]
```

### Example 2

```text
Input:  nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5
nums = [0,1,2,3,4,_,_,_,_,_]
```

## Approach

Since the array is already sorted, duplicate values appear next to each other.

We use the **Two Pointer** technique:

1. Keep pointer `i` at the position of the last unique element.
2. Use pointer `j` to scan the array from left to right.
3. If `nums[j]` is different from `nums[i]`, we found a new unique element.
4. Move `i` forward and place `nums[j]` at `nums[i]`.
5. Finally, return `i + 1` as the number of unique elements.

## Python 3 Solution

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1
```

## Complexity Analysis

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

The array is modified directly, so no additional array is required.

## Key Insight

Because the array is sorted, we don't need to search for duplicates. We simply compare each element with the **last unique element**.

The first `k` positions of the array will contain the required unique values.

## Constraints

* `1 <= nums.length <= 3 * 10^4`
* `-100 <= nums[i] <= 100`
* `nums` is sorted in non-decreasing order.

## Topic

**Arrays | Two Pointers | In-Place Algorithm**
