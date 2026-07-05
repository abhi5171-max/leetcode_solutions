# Group Anagrams

## Problem Statement

Given an array of strings, group the anagrams together.

Two strings are considered anagrams if they contain the same characters with the same frequencies.

The groups can be returned in any order.

### Example

**Input**

```text
strs = ["eat","tea","tan","ate","nat","bat"]
```

**Output**

```text
[
  ["bat"],
  ["nat","tan"],
  ["ate","eat","tea"]
]
```

---

## Approach

Use a **hash map** to group strings.

For every word:

* Sort its characters.
* Use the sorted string as the dictionary key.
* Append the original word to the corresponding group.

Since all anagrams produce the same sorted string, they naturally belong to the same group.

### Optimized Approach

Instead of sorting, create a frequency count of the 26 lowercase letters and use the frequency tuple as the key. This avoids sorting and improves the time complexity.

---

## Algorithm

1. Create an empty hash map.
2. Traverse every string.
3. Generate a key:

   * Sorted string, or
   * Character frequency tuple.
4. Store the original string in the corresponding group.
5. Return all grouped values.

---

## Complexity Analysis

### Sorting Approach

* **Time Complexity:** `O(n × k log k)`
* **Space Complexity:** `O(n × k)`

where:

* `n` = number of strings
* `k` = maximum length of a string

### Frequency Count Approach

* **Time Complexity:** `O(n × k)`
* **Space Complexity:** `O(n × k)`

---

## Key Concepts

* Hash Map
* Strings
* Sorting
* Character Frequency
* Grouping
