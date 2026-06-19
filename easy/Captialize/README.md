Codeforces 281A - Word Capitalization
Problem Statement

Given a word, capitalize its first letter. All other letters must remain unchanged.

Examples

Input

konjac

Output

Konjac

Input

ApPLe

Output

ApPLe
Approach
Read the input word.
Convert the first character to uppercase using upper().
Append the remaining part of the string unchanged.
Print the result.
Python Solution
word = input()

print(word[0].upper() + word[1:])
Complexity Analysis
Time Complexity: O(n)
Space Complexity: O(n)

where n is the length of the word.

Concepts Used
String Indexing
String Slicing
upper() Function