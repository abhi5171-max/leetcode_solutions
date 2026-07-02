1. George and Accommodation
Problem Summary

George and his friend Alex want to stay in the same dormitory room. Each room has a current number of occupants (p) and a maximum capacity (q). The goal is to determine how many rooms have space for both George and Alex.

Approach
Read the number of rooms.
For each room:
Calculate the available space using q - p.
If the available space is at least 2, count the room.
Print the total count.
Algorithm
Initialize a counter to 0.
Iterate through all rooms.
Check if q - p >= 2.
Increment the counter when the condition is true.
Output the counter.
Time Complexity
O(n)
Space Complexity
O(1)
Concepts Used
Loops
Conditional Statements
Counting
Simulation