# LeetCode 412 - Fizz Buzz

## Problem Statement

Given an integer `n`, return a string array `answer` (1-indexed) where:

* `answer[i] == "FizzBuzz"` if `i` is divisible by both 3 and 5.
* `answer[i] == "Fizz"` if `i` is divisible by 3.
* `answer[i] == "Buzz"` if `i` is divisible by 5.
* `answer[i] == str(i)` if none of the above conditions are true.

---

## Example

### Input

```python
n = 15
```

### Output

```python
["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
```

---

## Approach

We iterate through all numbers from `1` to `n`.

For each number:

1. Check if it is divisible by both `3` and `5`.

   * If yes, add `"FizzBuzz"` to the result list.
2. Otherwise, check if it is divisible by `3`.

   * If yes, add `"Fizz"`.
3. Otherwise, check if it is divisible by `5`.

   * If yes, add `"Buzz"`.
4. If none of the above conditions are true, add the number itself as a string.

The condition for divisibility by both `3` and `5` must be checked first to avoid classifying numbers like `15` as only `"Fizz"` or `"Buzz"`.

---

## Algorithm

1. Create an empty list `answer`.
2. Loop from `1` to `n`.
3. Apply the divisibility checks.
4. Append the appropriate string to the list.
5. Return the final list.

---

## Python Solution

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))

        return answer
```

---

## Complexity Analysis

### Time Complexity

**O(n)**

We iterate through the numbers from `1` to `n` exactly once.

### Space Complexity

**O(n)**

The output list stores `n` elements.

---

## Key Takeaways

* Use the modulo operator (`%`) to test divisibility.
* Always check the most specific condition (`3 and 5`) before the individual conditions.
* This problem is a classic introduction to loops and conditional statements.
