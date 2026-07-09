2. Tram

Problem: Find the minimum tram capacity required so that the number of passengers inside never exceeds the capacity.

Approach
Simulate the number of passengers inside the tram.
At each stop:
Remove exiting passengers.
Add entering passengers.
Track the maximum number of passengers present at any point.
The maximum passenger count is the required capacity.
Key Concepts
Simulation
Running Maximum

Time Complexity: O(n)
Space Complexity: O(1)