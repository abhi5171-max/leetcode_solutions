Problem Statement

Mike arranges magnets in a row.

Each magnet is represented as:

10
01

A new group is formed whenever the orientation changes from the previous magnet.

Determine the total number of groups.

Approach
The first magnet always starts the first group.
Compare every magnet with the previous one.
If they differ, increment the group count.
Algorithm
Read n.
Read the first magnet.
Initialize groups = 1.
For every remaining magnet:
Read current magnet.
If current != previous:
Increment groups.
Update previous magnet.
Print groups.
Time Complexity

O(n)

Space Complexity

O(1)

Concepts Used
String Comparison
Simulation
Sequential Traversal
Key Takeaways
Not every problem requires complex algorithms.
Simple simulations often provide the most efficient solution.
Comparing consecutive elements is a common and powerful technique in competitive programming.
Understanding problem constraints helps in choosing the simplest correct approach.