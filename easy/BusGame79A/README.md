🚌 A. Bus Game
Problem Summary

Ciel and Hanako play a game using:

x coins of 100 yen
y coins of 10 yen

Each player must take exactly 220 yen on their turn.

Player Strategies

Ciel prefers the maximum number of 100-yen coins:

2 × 100 + 2 × 10
1 × 100 + 12 × 10
22 × 10

Hanako prefers the maximum number of 10-yen coins:

22 × 10
1 × 100 + 12 × 10
2 × 100 + 2 × 10

If a player cannot take exactly 220 yen, that player loses.

Approach

Simulate the game turn by turn.

For each turn:

Check which valid combination the current player prefers.
Remove the required coins.
Switch turns.
If no combination is possible, the current player loses.
Complexity
Time: O(x + y) in the worst case
Space: O(1)
