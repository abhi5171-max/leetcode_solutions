# A. Rock-paper-scissors

## Problem Overview
Three players—Uncle Fyodor, Matroskin, and Sharic—play Rock-Paper-Scissors simultaneously. A player wins only if their gesture defeats the gestures shown by both of the other players. If no unique winner exists, output `?`.

## Approach
- Read the gestures of all three players.
- Handle three possible scenarios:
  1. All three gestures are the same → No winner.
  2. All three gestures are different → No winner.
  3. Exactly two players have the same gesture:
     - Identify the unique gesture.
     - Check if it beats the common gesture using the Rock-Paper-Scissors rules.
     - If yes, output the corresponding player's initial (`F`, `M`, or `S`); otherwise output `?`.

## Algorithm
1. Read the three gestures.
2. If all gestures are identical, print `?`.
3. If all gestures are different, print `?`.
4. Otherwise:
   - Determine the unique gesture and its owner.
   - Verify whether it beats the repeated gesture.
   - Print the winner if valid; otherwise print `?`.

## Complexity Analysis
- **Time Complexity:** `O(1)`
- **Space Complexity:** `O(1)`

## Key Concepts
- Conditional Statements
- Hash Map (Dictionary)
- Simulation