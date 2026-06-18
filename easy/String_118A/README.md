This is Codeforces Problem 118A - String Task.

Approach
Convert the entire string to lowercase.
Check each character:
If it is a vowel (a, o, y, e, u, i), skip it.
Otherwise, add "." + character to the result.
Print the result.
Python Solution
s = input().lower()

vowels = "aoyeui"
result = ""

for ch in s:
    if ch not in vowels:
        result += "." + ch

print(result)
Example

Input:

Codeforces

After lowercase:

codeforces

Remove vowels and add . before consonants:

.c.d.f.r.c.s

Output:

.c.d.f.r.c.s
Complexity
Time: O(n)
Space: O(n)

where n is the length of the string (≤ 100). This easily fits within the Limits.