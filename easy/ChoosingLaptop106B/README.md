💻 B. Choosing Laptop
Problem Summary

Vasya evaluates laptops using three properties:

Processor speed
RAM
HDD

A laptop is considered outdated if another laptop has strictly greater values in all three properties.

Among all laptops that are not outdated, Vasya chooses the cheapest one.

Approach

For every laptop:

Compare it with every other laptop.

If another laptop has:

greater processor speed,
greater RAM, and
greater HDD,

then mark the current laptop as outdated.

Otherwise, consider it as a candidate.
Select the candidate with the minimum cost.
Output its original index.
Complexity

There are at most 100 laptops, so checking every pair is sufficient.

Time: O(n²)
Space: O(n)