Problem

Given two integers n and m, where n is guaranteed to be prime, determine whether m is the immediate next prime number after n.

Approach
Implement a helper function to check if a number is prime.
Starting from n + 1, search for the first prime number.
Compare the first prime found with m.
Print "YES" if they are equal; otherwise print "NO".
Algorithm
Read n and m.
Define an is_prime() function.
Increment numbers after n until a prime is found.
Compare it with m.
Output the result.
Complexity
Time Complexity: O((m - n) × √m) (effectively constant since m ≤ 50)
Space Complexity: O(1)
Key Concepts
Prime Numbers
Brute Force Search
Number Theory