🤖 HQ9+
📌 Problem Overview

HQ9+ is a joke programming language with four instructions:

H → Prints Hello, World!
Q → Prints the program itself
9 → Prints the 99 Bottles of Beer song
+ → Increments an internal accumulator (produces no output)

Given a program, determine whether executing it produces any output.

💡 Approach

Only the instructions H, Q, and 9 generate output.

Simply check whether the input string contains any of these characters.

If yes, print "YES".
Otherwise, print **"NO"`.
🧠 Algorithm
Read the input string.
Check if it contains H, Q, or 9.
Print "YES" if any are present.
Otherwise, print "NO".
⏱ Complexity Analysis
Time Complexity: O(n)
Space Complexity: O(1)

where n is the length of the input string.

🛠 Concepts Used
String Traversal
Character Search
Conditional Statements
Implementation
🐍 Python Solution
p = input()

if 'H' in p or 'Q' in p or '9' in p:
    print("YES")
else:
    print("NO")