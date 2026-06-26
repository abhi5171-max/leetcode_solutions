Problem

Given the heights of n garden sections, determine the maximum number of sections that can be watered by creating artificial rain on exactly one section. Water flows to adjacent sections only if the next section's height is less than or equal to the current section's height.

Approach
For every section:
Expand to the left while the adjacent section is not higher.
Expand to the right while the adjacent section is not higher.
Count the total reachable sections.
Keep track of the maximum value.

Since n ≤ 1000, checking every section individually is efficient enough.

Algorithm
Read the input.
For each index:
Move left while height[left-1] <= height[left].
Move right while height[right+1] <= height[right].
Compute the watered section count.
Print the maximum count.
Complexity
Time Complexity: O(n²)
Space Complexity: O(1) (excluding the input array)
Key Concepts
Simulation
Array Traversal
Greedy Expansion