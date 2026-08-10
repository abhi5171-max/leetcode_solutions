
---

## README — A. Next Test

```markdown
# A. Next Test

## Problem

Polygon assigns an index to every test added to a programming problem.

The default index for the next test is defined as the **smallest positive integer that has not already been used**.

Given the indexes of all previously added tests, find the required default index.

## Approach

We can store all existing test indexes in a `set`.

Then check positive integers starting from `1`:

- If the number exists in the set, continue.
- The first number that does not exist is the answer.

Because there are `n` existing indexes, the answer will never need to be greater than `n + 1`.

## Example

### Input
```text
3
1 7 2