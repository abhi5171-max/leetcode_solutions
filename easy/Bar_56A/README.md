# A. Bar

## Problem
Determine the minimum number of people that must be checked to ensure no one under the age of 18 is consuming alcohol.

Alcoholic drinks:
- ABSINTH
- BEER
- BRANDY
- CHAMPAGNE
- GIN
- RUM
- SAKE
- TEQUILA
- VODKA
- WHISKEY
- WINE

## Approach
- Store all alcoholic drinks in a set for fast lookup.
- For each input:
  - If it is an age:
    - Count it if the age is less than 18.
  - If it is a drink:
    - Count it if it is an alcoholic drink.
- The final count is the minimum number of people that must be checked.

## Algorithm
1. Read the number of people.
2. Create a set containing all alcoholic drinks.
3. For each entry:
   - If it is numeric:
     - Convert it to an integer.
     - If age < 18, increment the answer.
   - Otherwise:
     - If it is an alcoholic drink, increment the answer.
4. Print the answer.

## Time Complexity
- **O(n)**

## Space Complexity
- **O(1)**

## Topics
- Strings
- Hash Set
- Simulation
- Implementation
```