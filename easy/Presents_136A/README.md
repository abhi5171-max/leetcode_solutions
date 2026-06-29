Problem

Given a mapping where friend i gives a gift to friend p[i], determine for every friend who gave them a gift.

Approach
The input represents a one-to-one mapping between gift givers and receivers.
Create an answer array.
For each friend i, assign:
answer[p[i] - 1] = i
This effectively computes the inverse permutation.
Algorithm
Read n.
Read the permutation p.
Initialize an array answer of size n.
Traverse p:
Store the giver for each receiver.
Print the answer array.
Complexity
Time Complexity: O(n)
Space Complexity: O(n)
Key Concepts
Arrays
Inverse Permutation
Simulation