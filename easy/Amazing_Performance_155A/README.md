Amazing Performance
Problem Overview

A coder participates in multiple programming contests, and their scores are recorded in chronological order. A performance is considered amazing if the coder achieves either:

A score higher than every previous score (new personal best), or
A score lower than every previous score (new personal worst).

The first contest is never considered amazing.

Approach
Initialize both the highest and lowest scores with the first contest's score.
Traverse the remaining scores:
If the current score is greater than the current maximum, increment the answer and update the maximum.
If the current score is smaller than the current minimum, increment the answer and update the minimum.
Print the total count of amazing performances.
Algorithm
Read the number of contests and their scores.
Set the first score as both the current maximum and minimum.
Iterate through the remaining scores.
Update records whenever a new maximum or minimum is found.
Output the total number of record-breaking performances.
Complexity Analysis
Time Complexity: O(n)
Space Complexity: O(1)
Key Concepts
Array Traversal
Minimum & Maximum Tracking
Simulation