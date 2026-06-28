Problem

Given an integer n, determine whether it is nearly lucky.

A number is nearly lucky if the number of lucky digits (4 and 7) in it is itself a lucky number (a number containing only digits 4 and 7).

Approach
Read the input as a string.
Count the occurrences of digits 4 and 7.
Check whether the count is a lucky number:
It must be greater than 0.
Every digit of the count must be either 4 or 7.
Print "YES" if the count is lucky; otherwise print "NO".
Algorithm
Input the number as a string.
Count all '4' and '7' characters.
If the count is 0, print "NO".
Otherwise, verify that every digit of the count is either 4 or 7.
Print the result.
Complexity
Time Complexity: O(n)
Space Complexity: O(1)
Key Concepts
String traversal
Counting
Digit manipulation