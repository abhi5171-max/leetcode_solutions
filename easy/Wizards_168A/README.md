# A. Wizards and Demonstration

## Problem

A city has **n** citizens, of which **x** are wizards who will definitely attend a demonstration. The administration reacts only if at least **y%** of the city's population participates.

The wizards can create clone puppets that count as participants. Determine the minimum number of clones required to ensure the demonstration reaches at least **y%** of the city's population.

## Approach

* Calculate the minimum number of participants needed using the ceiling of:

  `required = ceil(n × y / 100)`

* If the existing number of wizards is already sufficient, no clones are needed.

* Otherwise, create exactly the difference between the required participants and the number of wizards.

## Algorithm

1. Read `n`, `x`, and `y`.
2. Compute the required number of participants using ceiling division.
3. Calculate `required - x`.
4. If the result is negative, print `0`; otherwise, print the difference.

## Complexity Analysis

* **Time Complexity:** `O(1)`
* **Space Complexity:** `O(1)`

## Key Concepts

* Mathematics
* Percentage Calculation
* Ceiling Function
* Greedy Observation
