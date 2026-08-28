# A. Let's Watch Football

## Problem

Given:

* `a` — amount of data required to watch **1 second** of video.
* `b` — amount of data downloaded per second.
* `c` — length of the video in seconds.

It is guaranteed that:

```text
a > b
```

Since downloading is slower than watching, the guys need to wait some integer number of seconds before starting the video.

We need to find the **minimum waiting time** so that the video can be watched completely without any pauses.

---

## Key Observation

Suppose they wait `t` seconds.

During these `t` seconds, they download:

$$
t \times b
$$

units of data.

While watching the video, downloading continues. Since the download speed is `b` and the video requires `a` units per second, the total data available by the end of the video is:

$$
(t+c)b
$$

The complete video requires:

$$
ac
$$

units of data.

Therefore, we need:

$$
(t+c)b \geq ac
$$

Rearranging:

$$
tb + cb \geq ac
$$

$$
tb \geq c(a-b)
$$

$$
t \geq \frac{c(a-b)}{b}
$$

Since `t` must be an integer, we take the ceiling:

$$
\boxed{t = \left\lceil\frac{c(a-b)}{b}\right\rceil}
$$

The ceiling division can be calculated without floating point:

$$
\frac{x+y-1}{y}
$$

So:

```text
answer = (c * (a - b) + b - 1) // b
```

---

## Algorithm

1. Read `a`, `b`, and `c`.

2. Calculate the amount of additional data required because watching consumes data faster than downloading:

   ```text
   c * (a - b)
   ```

3. Divide by `b` and round up.

4. Print the result.

---

## Python Implementation

```python
a, b, c = map(int, input().split())

answer = (c * (a - b) + b - 1) // b

print(answer)
```

---

## Example 1

### Input

```text
4 1 1
```

The video requires:

$$
4 \times 1 = 4
$$

units of data.

If they wait `3` seconds, they download:

$$
3 \times 1 = 3
$$

units before watching.

During the 1-second video, they download one more unit, giving:

$$
3 + 1 = 4
$$

units.

Therefore, the answer is:

```text
3
```

---

## Example 2

### Input

```text
10 3 2
```

We calculate:

$$
t \geq \frac{2(10-3)}{3}
$$

$$
t \geq \frac{14}{3}
$$

Therefore:

$$
t = 5
$$

Output:

```text
5
```

---

## Example 3

### Input

```text
13 12 1
```

$$
t \geq \frac{1(13-12)}{12}
$$

$$
t \geq \frac{1}{12}
$$

The minimum integer value is `1`.

Output:

```text
1
```

---

## Complexity

The solution performs only a few arithmetic operations.

* **Time Complexity:** `O(1)`
* **Space Complexity:** `O(1)`

---

## Key Takeaway

When the download speed `b` is smaller than the playback requirement `a`, the guys need an initial buffer.

The required waiting time is:

```text
(c * (a - b) + b - 1) // b
```

This uses integer ceiling division and avoids floating-point precision issues.
