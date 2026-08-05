# A. Chat Room

## Problem
Determine whether the word **"hello"** can be obtained as a subsequence of the given string by deleting zero or more characters without changing the order of the remaining characters.

## Approach
- Store the target string `"hello"`.
- Traverse the input string.
- Maintain a pointer to the current character in `"hello"`.
- Whenever a matching character is found, move the pointer forward.
- If all characters of `"hello"` are matched, print `"YES"`; otherwise, print `"NO"`.

## Algorithm
1. Read the input string.
2. Initialize `target = "hello"` and pointer `j = 0`.
3. Iterate through each character of the input string.
4. If the current character matches `target[j]`, increment `j`.
5. After traversal:
   - If `j == len(target)`, print `"YES"`.
   - Otherwise, print `"NO"`.

## Time Complexity
- **O(n)**

## Space Complexity
- **O(1)**

## Topics
- Strings
- Two Pointers
- Greedy
- Subsequence