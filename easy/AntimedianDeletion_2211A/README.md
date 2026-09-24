# Codeforces - A. Antimedian Deletion

## Problem

You are given a permutation `p` of size `n`.

You can repeatedly choose any subarray of length `3` and delete either:

- the smallest element, or
- the largest element.

For every element `p[i]`, find the minimum possible length of the remaining array while still containing `p[i]`.

Each element is considered independently.

## Key Observation

Consider an element `x`.

### Case 1: `x = 1`

`1` is the smallest element in the entire permutation.

It can never be deleted because an operation can only delete the minimum or maximum of a chosen group of three. However, we can reduce all other elements around it until only `1` remains
