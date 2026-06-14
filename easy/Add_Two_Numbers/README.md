# Add Two Numbers

## Problem
Given two non-empty linked lists representing two non-negative integers, where digits are stored in reverse order, add the two numbers and return the sum as a linked list.

## Approach
Use a carry variable while traversing both linked lists simultaneously.

For each position:
1. Take the current digit from both lists (0 if a list has ended).
2. Add the digits and carry.
3. Create a new node with `sum % 10`.
4. Update carry as `sum // 10`.
5. Move to the next nodes.

A dummy node is used to simplify linked list construction.

## Complexity
- Time: O(max(m, n))
- Space: O(max(m, n))

## Example

Input:
l1 = [2,4,3]
l2 = [5,6,4]

Output:
[7,0,8]

Explanation:
342 + 465 = 807