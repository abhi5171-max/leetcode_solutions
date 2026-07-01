Arrival of the General
Problem Overview

A line of soldiers is arranged in arbitrary order based on their heights. The goal is to make:

The tallest soldier stand at the front of the line.
The shortest soldier stand at the end of the line.

Only adjacent swaps are allowed, and the task is to determine the minimum number of swaps required.

Approach
Find the leftmost occurrence of the tallest soldier since it requires the fewest swaps to move to the front.
Find the rightmost occurrence of the shortest soldier since it requires the fewest swaps to move to the end.
Calculate:
Swaps to move the tallest soldier to the front.
Swaps to move the shortest soldier to the end.
If the tallest soldier originally appears after the shortest soldier, subtract one swap because moving the tallest first shifts the shortest soldier one position closer to the end.
Algorithm
Read the number of soldiers and their heights.
Locate the leftmost maximum height.
Locate the rightmost minimum height.
Compute the total swaps.
Adjust the answer if the two movements overlap.
Print the minimum number of swaps.
Complexity Analysis
Time Complexity: O(n)
Space Complexity: O(1)
Key Concepts
Greedy Strategy
Array Indexing
Simulation
Adjacent Swaps