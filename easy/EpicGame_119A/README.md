🪨 Problem 1: Simon and Antisimon
Problem Summary

Simon and Antisimon each have a fixed positive integer and play a game with a pile of stones. On each turn, a player removes gcd(player_number, remaining_stones) stones. Simon moves first. A player loses if they cannot remove the required number of stones.

Approach
Simulate the game turn by turn.
On each move:
Compute the GCD of the player's fixed number and the remaining stones.
If the remaining stones are fewer than the required amount, the current player loses.
Otherwise, remove the stones and switch turns.
Continue until a winner is determined.
Algorithm
Read a, b, and n.
Start with Simon's turn.
Compute the required stones using gcd().
Check if the move is possible.
Remove stones and alternate turns.
Print:
0 if Simon wins.
1 if Antisimon wins.
Complexity
Time: O(n log n)
Space: O(1)
Concepts Used
Greatest Common Divisor (GCD)
Simulation
Game Theory