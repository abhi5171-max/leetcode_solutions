Problem: Two Sum

Given an integer array nums and an integer target, return the indices of the two numbers whose sum equals target.

Approach: Hash Map

Use a dictionary to store numbers and their indices.
For each number, compute its complement (target - num).
If the complement already exists in the dictionary, return the pair of indices.
Otherwise, store the current number and continue.

This approach achieves O(n) time complexity, making it much more efficient than the brute-force O(n²) solution.