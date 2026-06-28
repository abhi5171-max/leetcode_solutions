Problem

Given two binary strings of equal length, construct a new binary string where:

Output 1 if the corresponding bits are different.
Output 0 if the corresponding bits are the same.

This is equivalent to performing a bitwise XOR operation.

Approach
Read the two binary strings.
Compare characters at each position.
If they are equal, append 0; otherwise append 1.
Print the resulting string.
Algorithm
Input two binary strings.
Initialize an empty answer string.
Traverse both strings simultaneously.
Append:
0 if the characters are equal.
1 otherwise.
Output the final string.
Complexity
Time Complexity: O(n)
Space Complexity: O(n)
Key Concepts
String traversal
Character comparison
XOR logic