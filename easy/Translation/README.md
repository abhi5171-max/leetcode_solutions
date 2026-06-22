This problem asks whether the second string t is exactly the reverse of the first string s.

Approach
Read strings s and t.
Reverse s using slicing (s[::-1]).
Compare the reversed string with t.
Print "YES" if they are equal, otherwise print "NO".
Python 3 Solution
s = input().strip()
t = input().strip()

if s[::-1] == t:
    print("YES")
else:
    print("NO")
Example

Input:

code
edoc

Reversed "code" → "edoc" → matches t, so output:

YES
Complexity Analysis
Reversing a string of length n takes O(n) time.
Space complexity is O(n) for the reversed string.