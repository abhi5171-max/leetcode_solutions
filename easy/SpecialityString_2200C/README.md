# C. Specialty String — Python Solution

## Idea

In one operation, we choose a substring `s[l...r]` where **all characters are the same**, and replace that entire substring with `*`.

So the operation can be applied independently to every **consecutive group of equal characters**.

To win, eventually every character must become `*`. Therefore, **every character must belong to a group of length at least 2**.

So the answer is:

* `YES` if the string can be completely divided into blocks of equal characters, each having length **at least 2**.
* `NO` otherwise.

For example:

```text
llmllm
```

Groups:

```text
ll | m | ll | m
```

There are groups of length `1`, but after replacing the `ll` groups, the remaining `m` characters can become adjacent and form `mm`. Hence, the process can continue.

This means we need to consider that after deleting a group, neighboring equal characters can merge.

A convenient way is to repeatedly process the string using a stack. A character can be removed whenever it becomes part of a pair.

### Python Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    stack = []

    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
```

### Why does this work?

Whenever two equal characters become adjacent, they can be removed together.

For example:

```text
llmllm
```

Process:

```text
llmllm
 ↓
mllm
 ↓
mm
 ↓
empty
```

Therefore, the answer is `YES`.

For:

```text
byebye
```

There is no way to make all characters disappear, so the stack remains non-empty and the answer is `NO`.

### Complexity

For each test case:

* **Time:** `O(n)`
* **Space:** `O(n)`

Since the sum of `n` over all test cases is bounded, this easily fits within the limits.
