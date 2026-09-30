# A. Eating Game — Solution

## Key observation

Let the total number of dishes be:

$$
S = a_1+a_2+\cdots+a_n
$$

Suppose player `i` starts the game.

The turns are cyclic, so the player who eats the **last dish** depends on the starting position and on how many dishes each player has.

A player `i` can be the winner exactly when:

$$
a_i = \max(a_1,a_2,\ldots,a_n)
$$

**Why?**

The player with the maximum number of dishes can be made to eat the final dish by choosing a suitable starting player. Players with fewer dishes cannot always survive until the final turn.

Therefore, the answer is simply the **number of players having the maximum number of dishes**.

### Example

For:

```text
1 4 3 4
```

Maximum dishes:

```text
4
```

Players having 4 dishes = **2**

So the answer is:

```text
2
```

---

## Python Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    maximum = max(a)
    answer = a.count(maximum)

    print(answer)
```

### Complexity

* **Time:** `O(n)` per test case
* **Space:** `O(n)`

### Sample

```text
Input:
3
1
10
2
6 7
4
1 4 3 4
```

```text
Output:
1
1
2
```
