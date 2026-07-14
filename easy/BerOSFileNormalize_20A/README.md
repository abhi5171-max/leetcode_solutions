# BerOS File Path Normalization

## Problem
The BerOS operating system allows multiple consecutive `/` characters to act as a single path separator. Additionally, trailing slashes should only remain if the path represents the root directory (`/`).

Given a file path, normalize it by:
- Replacing consecutive `/` characters with a single `/`.
- Removing the trailing `/` unless the path is the root directory.

## Approach
1. Traverse the input string character by character.
2. When a `/` is encountered:
   - Add a single `/` to the result.
   - Skip all consecutive `/` characters.
3. Copy all other characters directly.
4. Remove the trailing `/` if the normalized path is not the root directory.
5. Print the normalized path.

## Algorithm
- Read the input path.
- Iterate through the string.
- Compress consecutive slashes into one.
- Remove the trailing slash when necessary.
- Output the normalized path.

## Complexity Analysis
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

## Concepts Used
- Strings
- Iteration
- String construction