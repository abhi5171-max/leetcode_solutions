README – Caps Lock
Problem

Sometimes the Caps Lock key is accidentally enabled while typing.

A word is considered incorrectly typed if:

All letters are uppercase, or
All letters except the first are uppercase.

If either condition is true, change the case of every letter. Otherwise, leave the word unchanged.

Approach

Python provides useful built-in string methods:

isupper() – Checks whether all letters are uppercase.
islower() – Checks whether a letter is lowercase.
swapcase() – Converts uppercase letters to lowercase and vice versa.

We check:

If the entire word is uppercase.
Or, if the first letter is lowercase and the remaining letters (word[1:]) are all uppercase.

If either condition is satisfied, use swapcase() to flip the case of every character.

Algorithm
Read the input word.
If:
word.isupper() is True, or
word[0].islower() and word[1:].isupper() are both True,
then print word.swapcase().
Otherwise, print the original word.
Complexity
Time Complexity: O(n)
Space Complexity: O(n)

where n is the length of the word.

Python Solution
word = input()

if word.isupper() or (word[0].islower() and word[1:].isupper()):
    print(word.swapcase())
else:
    print(word)
Example
Input
cAPS
Output
Caps
Explanation
The first character is lowercase.
Every remaining character is uppercase.
Therefore, the case of every character is reversed.