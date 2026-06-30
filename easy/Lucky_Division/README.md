🍀 Almost Lucky
📌 Problem Overview

A number is called lucky if its decimal representation contains only the digits 4 and 7.

A number is almost lucky if it is divisible by at least one lucky number.

Given an integer n, determine whether it is almost lucky.

💡 Approach
Generate all lucky numbers from 1 to 1000.
A number is lucky if every digit is either 4 or 7.
Check whether the given number is divisible by any generated lucky number.
If divisible, print "YES"; otherwise, print "NO".
🧠 Algorithm
Read the integer n.
Iterate through numbers from 1 to 1000.
Store numbers containing only digits 4 and 7.
Check if n % lucky_number == 0.
Print the result.
⏱ Complexity Analysis
Time Complexity: O(1000)
Space Complexity: O(1)

The constraints are small, making this brute-force approach efficient.

🛠 Concepts Used
Brute Force
Number Theory
Divisibility
String Processing
🐍 Python Solution
n = int(input())

lucky_numbers = []

for i in range(1, 1001):
    if all(c in "47" for c in str(i)):
        lucky_numbers.append(i)

for num in lucky_numbers:
    if n % num == 0:
        print("YES")
        break
else:
    print("NO")