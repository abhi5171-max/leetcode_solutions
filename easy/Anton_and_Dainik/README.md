Problem

Anton and Danik played n chess games. Each game has exactly one winner:

A → Anton won
D → Danik won

Determine who won more games or whether they won an equal number.

Approach
Count the occurrences of:
'A' for Anton's wins.
'D' for Danik's wins.
Compare the counts:
If Anton has more wins, print "Anton".
If Danik has more wins, print "Danik".
Otherwise, print "Friendship".
Algorithm
Read n and the result string.
Count 'A' and 'D'.
Compare the counts.
Print the appropriate result.
Complexity
Time Complexity: O(n)
Space Complexity: O(1)
Key Concepts
String Processing
Character Counting
Conditional Statements