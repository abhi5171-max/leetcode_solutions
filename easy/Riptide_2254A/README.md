# A. Riptide

## Problem

Alice, Bob, and Charlie start with `a`, `b`, and `c` tokens respectively.

The game is played in rounds:

1. Before each round, if any two players have the same number of tokens, the game ends.
2. Otherwise, the player with the most tokens gives exactly `1` token to the player with the fewest tokens.

Given the starting number of tokens, determine how many rounds the game lasts before it ends.

---

## Approach

We can solve this problem by directly simulating the game.

For each round:

* Check whether all three token counts are different.
* Find the player with the maximum number of tokens.
* Find the player with the minimum number of tokens.
* Transfer `1` token from the maximum to the minimum.
* Increase the round counter.

The game stops as soon as any two players have the same number of tokens.

---

## Algorithm

1. Store `a`, `b`, and `c` in a list.
2. Initialize `rounds = 0`.
3. While all three token counts are different:

   * Find the index of the maximum value.
   * Find the index of the minimum value.
   * Decrease the maximum value by `1`.
   * Increase the minimum value by `1`.
   * Increment `rounds`.
4. Print `rounds`.

---

## Complexity

Since the token values are very small, simulation is efficient.

* **Time Complexity:** `O(rounds)` per test case
* **Space Complexity:** `O(1)`

---

## Python 3 Solution

```python
import sys


def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        tokens = list(map(int, input().split()))
        rounds = 0

        while len(set(tokens)) == 3:
            max_index = tokens.index(max(tokens))
            min_index = tokens.index(min(tokens))

            tokens[max_index] -= 1
            tokens[min_index] += 1

            rounds += 1

        print(rounds)


if __name__ == "__main__":
    solve()
```

---

## Example

### Input

```text
1
1 7 10
```

### Simulation

```text
1 7 10 → 2 7 9   Round 1
2 7 9  → 3 7 8   Round 2
3 7 8  → 4 7 7   Round 3
```

Now Bob and Charlie both have `7` tokens.

### Output

```text
3
```
