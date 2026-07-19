A. Power Consumption Calculation
📌 Problem

A laptop operates in three power modes:

Normal Mode: Consumes P1 watts per minute.
Screensaver Mode: Starts after T1 minutes of inactivity and consumes P2 watts per minute.
Sleep Mode: Starts T2 minutes after the screensaver begins and consumes P3 watts per minute.

Given Tom's working intervals, compute the total power consumed during the entire period from the beginning of the first interval to the end of the last interval.

💡 Approach
Add the power consumed during every active working interval using the normal power consumption.
For every idle gap between two consecutive working intervals:
Spend the first T1 minutes in Normal Mode.
Spend the next T2 minutes in Screensaver Mode.
Spend any remaining time in Sleep Mode.
Sum the consumption from all intervals and idle gaps.
✅ Algorithm
Read all work intervals.
For each interval:
Add active power consumption.
For each gap between consecutive intervals:
Calculate power consumed in Normal Mode.
Calculate power consumed in Screensaver Mode.
Calculate power consumed in Sleep Mode.
Print the total power consumption.
⏱️ Complexity
Time Complexity: O(n)
Space Complexity: O(1) (excluding the input storage)
🛠️ Concepts Used
Simulation
Greedy Processing
Conditional Logic
Interval Processing
Implementation