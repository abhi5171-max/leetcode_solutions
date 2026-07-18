# A. Almost Prime

## Problem
A number is called **almost prime** if it has **exactly two distinct prime divisors**.

Given an integer `n`, count how many almost prime numbers exist between `1` and `n` (inclusive).

## Approach
- Use a sieve-like algorithm to count the number of distinct prime divisors for every number.
- Every time a prime is found, increment the divisor count of all its multiples.
- Finally, count how many numbers have exactly two distinct prime divisors.

## Algorithm
1. Create an array `divisors` initialized with `0`.
2. Iterate from `2` to `n`.
3. If `divisors[i] == 0`, then `i` is prime.
4. Increment the divisor count for every multiple of `i`.
5. Count numbers where `divisors[i] == 2`.
6. Print the count.

## Complexity
- **Time Complexity:** `O(n log log n)`
- **Space Complexity:** `O(n)`

## Example

### Input
```
21
```

### Output
```
8
```

## Key Concepts
- Sieve of Eratosthenes
- Prime Numbers
- Number Theory
- Distinct Prime Divisors
```