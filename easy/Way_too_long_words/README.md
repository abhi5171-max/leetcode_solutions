A. Way Too Long Words
Problem Description

Some words are so long that writing them repeatedly becomes inconvenient. A word is considered too long if its length is greater than 10 characters.

For every such word, replace it with an abbreviation formed by:

The first letter of the word.
The number of characters between the first and last letters.
The last letter of the word.
Examples
localization → l10n
internationalization → i18n

Words with length 10 or less remain unchanged.

Approach

For each word:

Check its length using len(word).
If the length is greater than 10:
Print the first character.
Print the count of middle characters (len(word) - 2).
Print the last character.
Otherwise, print the word as it is.
Python 3 Solution
n = int(input())

for _ in range(n):
    word = input()

    if len(word) > 10:
        print(word[0] + str(len(word) - 2) + word[-1])
    else:
        print(word)
Example
Input
4
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis
Output
word
l10n
i18n
p43s
Complexity Analysis
Time Complexity: O(n × m)
n = number of words
m = average length of a word
Space Complexity: O(1)
Only a few variables are used regardless of input size.
Key Concept

String manipulation and conditional checking based on word length. This problem is a simple introduction to handling strings efficiently in competitive programming.