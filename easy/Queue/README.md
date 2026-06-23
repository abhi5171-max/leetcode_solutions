
### 1. Queue at the School (266B)

#### Problem Summary

Children are standing in a queue represented by a string consisting of `B` (boys) and `G` (girls). Every second, whenever a boy is immediately followed by a girl (`BG`), they swap positions. The task is to determine the arrangement after `t` seconds.

#### Approach

* Convert the string into a list for easy swapping.
* Simulate the process for `t` seconds.
* Traverse the queue from left to right.
* Whenever a `BG` pair is found, swap them and skip the next position to prevent multiple moves in the same second.

#### Time Complexity

* **O(n × t)**

#### Space Complexity

* **O(n)**

---

