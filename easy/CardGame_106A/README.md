# A. Card Game

## Problem Statement
Given the trump suit and two cards, determine whether the **first card beats the second card** according to the rules of the card game **Durak**.

A card beats another card if:
- Both cards have the same suit and the first has a higher rank.
- The first card is a trump card and the second is not.

## Approach
- Store the card ranks in increasing order.
- Compare suits:
  - If suits are the same, compare their ranks.
  - Otherwise, check whether the first card is a trump card.
- Print `"YES"` if the first card beats the second card; otherwise print `"NO"`.

## Algorithm
1. Read the trump suit.
2. Read both cards.
3. If both cards have the same suit:
   - Compare their ranks.
4. Else:
   - If the first card is trump and the second isn't → `YES`
   - Otherwise → `NO`

## Complexity Analysis
- **Time Complexity:** `O(1)`
- **Space Complexity:** `O(1)`

## Python Solution

```python
trump = input().strip()
card1, card2 = input().split()

order = "6789TJQKA"

rank1, suit1 = card1[0], card1[1]
rank2, suit2 = card2[0], card2[1]

if suit1 == suit2:
    if order.index(rank1) > order.index(rank2):
        print("YES")
    else:
        print("NO")
elif suit1 == trump and suit2 != trump:
    print("YES")
else:
    print("NO")
```

## Key Concepts
- Strings
- Simulation
- Conditional Logic
- Card Ranking