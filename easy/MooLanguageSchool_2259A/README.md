# Codeforces — A. Moo Language School

## Problem

Farmer John wants to build schools in `n` fields.

The fields are divided into farms, where each farm contains exactly `k` consecutive fields.

There are:

* `n` total fields
* `n / k` farms
* `k` fields in each farm

If a field contains `1`, it belongs to Farmer Nhoj, so building a school there costs extra.

Farmer John needs to build **at least one school in every farm** and wants to minimize the number of schools built on Nhoj's land.

---

## Key Observation

We can consider each farm independently.

For every group of `k` consecutive fields:

* If the group contains at least one `0`, Farmer John can build the school on that field without paying Nhoj.
* If the entire group consists of `1`s, every field belongs to Nhoj, so Farmer John is forced to build one school on Nhoj's land.

Therefore:

> **The answer is the number of farms whose `k` fields are all `1`.**

---

## Example

### Input

```text
6
8 2
10011100
5 1
11111
8 4
01111110
5 1
00101
4 4
1101
4 4
1111
```

Divide the first test case into groups of `k = 2`:

```text
10 | 01 | 11 | 00
```

Only `11` contains no `0`, so we must build one school on Nhoj's land.

Answer:

```text
1
```

For the second test case:

```text
11111
```

Since `k = 1`, every farm contains a `1`, so all 5 schools must be built on Nhoj's land.

Answer:

```text
5
```

---

## Algorithm

For every test case:

1. Read `n`, `k`, and the binary string `s`.
2. Start `answer = 0`.
3. Divide `s` into groups of `k` characters.
4. For each group:

   * If it contains no `0`, increment `answer`.
5. Print `answer`.

### Python Implementation

```python
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()

    answer = 0

    for i in range(0, n, k):
        farm = s[i:i + k]

        if '0' not in farm:
            answer += 1

    print(answer)
```

---

## Complexity

There are `n` fields in each test case, and every field is examined once.

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(k)` for the farm substring.

---

## Key Takeaway

The problem looks like a school-placement problem, but there is no need to actually construct the schools.

Simply:

> **Count the groups of `k` consecutive fields that contain only `1`s.**

Those are exactly the farms where Farmer John has no choice but to build a school on Farmer Nhoj's land.


