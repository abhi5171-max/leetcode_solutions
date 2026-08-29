# A. Exams

## Problem Statement

The author has `n` exams. For each exam, he can choose a mark from **2 to 5**.

He wants the sum of all marks to be exactly `k`, while minimizing the number of exams with mark `2` because a mark of `2` means he must re-sit that exam.

Find the **minimum number of exams** that receive a mark of `2`.

## Approach

To minimize the number of failed exams:

* Start by giving every exam the highest possible passing mark, `5`.
* The initial sum is `5 × n`.
* We need to reduce this sum to exactly `k`.
* Changing a mark from:

  * `5 → 4` reduces the sum by `1`
  * `5 → 3` reduces the sum by `2`
  * `5 → 2` reduces the sum by `3`

A mark of `2` gives the **largest possible reduction (3)** while using only one exam.

Therefore, we should use as many `2`s as necessary, while making the remaining marks `3`, `4`, or `5`.

A convenient way to calculate the answer is:

* If `5n - k` is the amount we need to reduce.
* Every exam changed to `2` can reduce the sum by at most `3`.
* Therefore, the minimum number of exams receiving `2` is:

```text
ceil((5n - k) / 3)
```

## Python Solution

```python id="x7c4m2"
n, k = map(int, input().split())

difference = 5 * n - k

answer = (difference + 2) // 3

print(answer)
```

## Example 1

### Input

```text
4 8
```

Initially, all exams have mark `5`:

```text
5 + 5 + 5 + 5 = 20
```

We need to reduce the sum by:

```text
20 - 8 = 12
```

Each mark `2` reduces the sum by `3`:

```text
2 + 2 + 2 + 2 = 8
```

So all four exams must be re-sit.

### Output

```text
4
```

## Example 2

### Input

```text
4 10
```

We need to reduce:

```text
20 - 10 = 10
```

Two exams can receive `2`, reducing the sum by `6`. The remaining two can receive `3`, reducing it by another `4`:

```text
2 + 2 + 3 + 3 = 10
```

Therefore, the minimum number of re-sits is `2`.

### Output

```text
2
```

## Example 3

### Input

```text
1 3
```

The only exam receives mark `3`, so no exam needs to be re-sit.

### Output

```text
0
```

## Complexity

* **Time:** `O(1)`
* **Space:** `O(1)`

## Key Concept

Start from the maximum possible total `5n`. The required reduction is `5n - k`, and each exam marked `2` can reduce the total by at most `3`.

Thus:

```text
answer = ceil((5n - k) / 3)
```

In integer arithmetic:

```python
(5 * n - k + 2) // 3
```
