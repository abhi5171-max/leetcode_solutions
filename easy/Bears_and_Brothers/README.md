Problem Statement

Limak wants to become strictly heavier than his brother Bob.

Initially:

Limak weighs a
Bob weighs b (a ≤ b)

Every year:

Limak's weight becomes 3 × current weight
Bob's weight becomes 2 × current weight

Determine how many full years it takes for Limak to become strictly heavier than Bob.

Approach
Read the initial weights.
Simulate each year:
Triple Limak's weight.
Double Bob's weight.
Count the number of years.
Stop once Limak's weight becomes greater than Bob's.
Algorithm
Read a and b.
Initialize years = 0.
While a <= b:
a *= 3
b *= 2
years += 1
Print years.
Time Complexity

O(years)

Space Complexity

O(1)

Concepts Used
Simulation
While Loop
Basic Arithmetic