# Anonymous Letter

## Problem

Given a newspaper heading and a target letter, determine whether the letter can be formed by cutting characters from the heading. Each non-space character in the heading can be used at most once, while spaces do not need to be cut and can be inserted freely.

## Example

**Input**

```text
Instead of dogging Your footsteps it disappears but you dont notice anything
Your dog is upstears
```

**Output**

```text
YES
```

## Approach

* Ignore spaces in both the heading and the target text.
* Count the frequency of every character in the heading.
* Traverse the target text:

  * If a required character is unavailable, output **NO**.
  * Otherwise, consume one occurrence of that character.
* If every character is successfully matched, output **YES**.

## Algorithm

1. Read the heading and target text.
2. Count all non-space characters in the heading.
3. Iterate through the target text while ignoring spaces.
4. Check and update character frequencies.
5. Print **YES** if all characters are available; otherwise, print **NO**.

## Complexity

* **Time Complexity:** `O(n + m)`
* **Space Complexity:** `O(k)` where `k` is the number of distinct characters.

## Key Concepts

* Hash Maps / Frequency Counting
* String Manipulation
* Character Matching
* Case Sensitivity
