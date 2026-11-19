# Codeforces - A. False Alarm

**Platform:** Codeforces  
**Problem:** A. False Alarm  
**Language:** Python 3  
**Topics:** Greedy, Arrays, Implementation

## Problem Statement

Yousef needs to pass through `n` doors in a hallway.

- An open door (`0`) takes one second to pass.
- A closed door (`1`) cannot be passed normally.
- Yousef has a special button that can be used at most once.
- When activated, the button opens all closed doors for `k` seconds.

Determine whether Yousef can pass through all the doors and reach the exit.

## Approach: Greedy + Array Traversal

The important observation is that Yousef only needs to activate the button when he reaches the first closed door.

The button must remain active until he passes the last closed door.

### Step 1: Find the first closed door

Find the first occurrence of `1` in the array.

### Step 2: Find the last closed door

Find the last occurrence of `1` in the array.

### Step 3: Calculate the required duration

The number of seconds needed to pass from the first closed door to the last closed door is:

`required_time = last - first + 1`

### Step 4: Check the condition

- If `required_time <= k`, print `YES`.
- Otherwise, print `NO`.

**Final Condition:**

`last - first + 1 <= k`

## Python 3 Solution

```python
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    first = a.index(1)
    last = n - 1 - a[::-1].index(1)

    if last - first + 1 <= k:
        print("YES")
    else:
        print("NO")
```

## Example

**Input:**

```text
7
4 2
0 1 1 0
6 3
1 0 1 1 0 0
8 8
1 1 1 0 0 1 1 1
1 2
1
5 1
1 0 1 0 1
7 4
0 0 0 1 1 0 1
10 3
0 1 0 0 1 0 0 1 0 0
```

**Output:**

```text
YES
NO
YES
YES
NO
YES
NO
```

## Dry Run

Consider:

`n = 4, k = 2`

`a = [0, 1, 1, 0]`

- First closed door index = 1
- Last closed door index = 2
- Required time = `2 - 1 + 1 = 2`
- Available button duration = 2 seconds.

Since `2 <= 2`, the answer is `YES`.

## Complexity Analysis

- **Time Complexity:** `O(n)` per test case because we traverse the array to find the first and last closed doors.
- **Space Complexity:** `O(n)` for storing the input array.

## Key Learnings

- Finding the first and last occurrences of an element.
- Applying greedy reasoning to minimize button usage.
- Converting a movement problem into a simple range calculation.
- Using array traversal efficiently.

---

**Final Observation:**

Only the distance between the first and last closed doors matters. If the button duration covers this entire interval, Yousef can successfully pass through all doors.