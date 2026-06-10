# Roman to Integer

Given a Roman numeral string, convert it to its integer value.

## Approach

Use a hash map to store the value of each Roman symbol.

Traverse the string from left to right:

- If the current symbol is smaller than the next symbol, subtract its value.
- Otherwise, add its value.

This handles both normal Roman numerals and subtraction cases such as:
- IV = 4
- IX = 9
- XL = 40
- XC = 90
- CD = 400
- CM = 900

## Complexity

- Time: O(n)
- Space: O(1)

## Example

Input:

MCMXCIV


Output:

1994