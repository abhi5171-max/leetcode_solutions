⏰ Problem 2: Next Palindrome Time
Problem Summary

Given a time in HH:MM format, find the next time (strictly after the current one) whose digits form a palindrome.

Approach
Increment the time one minute at a time.
Handle transitions between minutes, hours, and days.
Check whether the four digits (HHMM) read the same forwards and backwards.
Output the first palindromic time encountered.
Algorithm
Parse the input time.
Increase the time by one minute.
Wrap minutes after 59 and hours after 23.
Convert the time into a four-digit string.
If the string equals its reverse, print the time and stop.
Complexity
Time: O(1440) (at most one full day)
Space: O(1)
Concepts Used
String Manipulation
Simulation
Time Arithmetic