# A. You Delete, I Delete

## Problem Statement

Alice and Bob are given a binary string containing at least one `0` and one `1`.

They perform one operation each:

1. Alice deletes one occurrence of `0`.
2. Bob then deletes one occurrence of `1`.

Alice wants the final string to be **lexicographically largest**, while Bob wants it to be **lexicographically smallest**.

Determine the final string when both players play optimally.

---

## Approach

For every possible `0` that Alice can delete:

1. Create the remaining string after deleting that `0`.
2. Bob optimally deletes the **first occurrence of `1`** to make the string lexicographically smallest.
3. Compare the resulting string with the best answer found so far.
4. Keep the lexicographically largest result.

---

## Algorithm

For each test case:

* Initialize an empty string `best`.
* Iterate through every character of the string.
* If the character is `0`:

  * Delete it.
  * Find and delete the first `1` from the remaining string.
  * Update `best` if the resulting string is lexicographically larger.
* Print `best`.

---

## Complexity Analysis

* **Time Complexity:** `O(n²)`
* **Space Complexity:** `O(n)`

---

## Example

### Input

```text
4
101
11001
0010
0101010000010100100101
```

### Output

```text
1
101
00
01010000010100100101
