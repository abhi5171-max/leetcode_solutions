# A. Cifera

## Problem

Petya invents a word **petricium** that represents a number `k`.

The expressions:

* `petricium` → (k)
* `petricium la petricium` → (k^2)
* `petricium la petricium la petricium` → (k^3)

and so on.

Given integers `k` and `l`, determine whether `l` can be represented as a power of `k`. If it can, output the number of `la` articles in its representation.

## Approach

We repeatedly divide `l` by `k` while it is divisible by `k`.

If `l` eventually becomes `1`, then:

[
l = k^p
]

where `p` is the number of `petricium` words.

The number of `la` articles is:

[
p - 1
]

## Algorithm

1. Read `k` and `l`.
2. Set `count = 0`.
3. While `l` is divisible by `k`:

   * Divide `l` by `k`.
   * Increment `count`.
4. If `l == 1`:

   * Print `YES`.
   * Print `count - 1`.
5. Otherwise, print `NO`.

## Complexity

* **Time:** (O(\log_k l))
* **Space:** (O(1))

## Example

### Input

```text
5
25
```

### Output

```text
YES
1
```

Because:

[
25 = 5^2
]

Therefore, the representation contains one `la`.

## Language

**Python 3**
