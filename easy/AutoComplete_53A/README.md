# Autocomplete

## Problem

Given a prefix `s` and a list of previously visited page addresses, print the **lexicographically smallest** address that starts with `s`. If no such address exists, print `s`.

### Example

**Input**

```
next
2
nextpermutation
nextelement
```

**Output**

```
nextelement
```

## Approach

* Iterate through all visited pages.
* Check whether each page starts with the given prefix using `startswith()`.
* Among all matching pages, keep the lexicographically smallest one.
* If no page matches, print the original prefix.

## Algorithm

1. Read the prefix `s`.
2. Read all visited page addresses.
3. For each address:

   * If it starts with `s`, compare it with the current best answer.
4. Print the smallest matching address.
5. If no match exists, print `s`.

## Complexity

* **Time Complexity:** `O(n × m)` where `m` is the maximum string length.
* **Space Complexity:** `O(1)` extra space.

## Key Concepts

* String Prefix Matching
* Lexicographical Ordering
* Linear Search
