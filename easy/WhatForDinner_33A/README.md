# A. What is for dinner?

## Problem

Valerie the shark has several rows of teeth. Each tooth has a certain residual viability, which represents how many crucians can be eaten using that tooth.

When Valerie eats one crucian using a particular row:

- Every tooth in that row loses `1` viability.
- A tooth cannot have negative viability.

For each row, the maximum number of crucians that can be eaten using that row is therefore equal to the **minimum viability among all teeth in that row**.

Given the total number of available crucians `k`, find the maximum number of crucians Valerie can eat.

## Approach

1. Maintain the minimum viability for every tooth row.
2. For each tooth `(r, c)`, update:
   ```text
   min_viability[r] = min(min_viability[r], c)