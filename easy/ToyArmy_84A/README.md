# Codeforces — A. Toy Army

## Problem

In the game **GAGA**, two armies each contain `n` soldiers, where `n` is even.

The game has three turns:

1. Valera attacks Arcady's army.
2. Arcady attacks Valera's army.
3. Valera attacks Arcady's remaining army.

A soldier can target any enemy soldier, and multiple soldiers can target the same soldier. We need to determine the **maximum possible number of soldiers killed** after all three turns.

## Approach

Suppose Valera kills `x` soldiers in the first turn.

* Arcady has `n - x` soldiers remaining.
* In the second turn, Arcady can kill at most `n - x` soldiers.
* Valera therefore has `x` soldiers remaining.
* In the third turn, Valera can kill at most `min(x, n - x)` soldiers.

Therefore:

```text
Total = x + (n - x) + min(x, n - x)
      = n + min(x, n - x)
```

The value of `min(x, n - x)` is maximum when:

```text
x = n / 2
```

Hence:

```text
Answer = n + n/2
       = 3n/2
```

Since `n` is guaranteed to be even, the result is always an integer.

## Complexity

* **Time:** `O(1)`
* **Space:** `O(1)`

## Python 3

```python
n = int(input())

print(3 * n // 2)
```

## Examples

### Input

```text
2
```

### Output

```text
3
```

### Input

```text
4
```

### Output

```text
6
```


