# A. Blackjack

## Problem

A standard deck contains 52 cards. The player has already received the **queen of spades**, which is worth **10 points**.

The player wins if the total value of the two cards is exactly `n`.

We need to determine how many possible second cards can produce the required total.

### Card Values

| Card  |  Points | Number of Cards |
| ----- | ------: | --------------: |
| 2–9   |     2–9 |          4 each |
| 10    |      10 |               4 |
| Jack  |      10 |               4 |
| Queen |      10 |               4 |
| King  |      10 |               4 |
| Ace   | 1 or 11 |               4 |

The queen of spades has already been used, so it cannot be selected again.

---

## Approach

The first card is always worth `10`.

Therefore, the second card must provide:

```text
required = n - 10
```

We check the required value:

### 1. Values from 2 to 9

There are exactly **4 cards** for every value.

So if:

```text
2 <= required <= 9
```

the answer is:

```text
4
```

### 2. Cards worth 10

There are four tens, four jacks, four queens, and four kings:

```text
4 × 4 = 16
```

However, the **queen of spades** is already in the player's hand.

Therefore:

```text
16 - 1 = 15
```

If:

```text
required == 10
```

the answer is `15`.

### 3. Ace

An ace can be worth either `1` or `11`.

Therefore, there are 4 valid aces if:

```text
required == 1
```

or:

```text
required == 11
```

### 4. All other values

No card can provide the required number of points.

The answer is `0`.

---

## Python 3 Solution

```python
n = int(input())

required = n - 10

if 2 <= required <= 9:
    print(4)
elif required == 10:
    print(15)
elif required == 1 or required == 11:
    print(4)
else:
    print(0)
```

---

## Complexity

The solution performs only a few comparisons.

```text
Time Complexity:  O(1)
Space Complexity: O(1)
```

---

## Example 1

### Input

```text
12
```

The queen gives `10` points.

We need:

```text
12 - 10 = 2
```

There are four `2`s in the deck, one for each suit.

### Output

```text
4
```

---

## Example 2

### Input

```text
20
```

We need:

```text
20 - 10 = 10
```

Cards worth 10 points are:

* 4 tens
* 4 jacks
* 4 queens
* 4 kings

That gives:

```text
16 cards
```

But the queen of spades is already used.

Therefore:

```text
16 - 1 = 15
```

### Output

```text
15
```

---

## Example 3

### Input

```text
10
```

We need:

```text
10 - 10 = 0
```

No card is worth zero points.

### Output

```text
0
```

---

## Key Takeaway

The problem becomes very simple once we remember that the first card, the queen of spades, is always worth `10`.

So we only need to determine which card values equal:

```text
n - 10
```

and account for the fact that the queen of spades has already been removed from the deck.

## Tags

* Codeforces
* Implementation
* Case Analysis
* Beginner
* Python 3
* Blackjack
