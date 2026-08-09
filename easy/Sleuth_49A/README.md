# Codeforces A. Sleuth

## Problem Statement

Vasya is playing a sleuth game where his friends answer his questions according to a fixed rule:

* If the **last letter** of the question is a vowel, the answer is `YES`.
* If the **last letter** is a consonant, the answer is `NO`.

The English vowels are:

```text
A, E, I, O, U, Y
```

The question may contain uppercase and lowercase letters, spaces, and a question mark.

The task is to determine the answer based on the **last letter**, ignoring spaces and the question mark.

---

## Approach

1. Read the complete question.
2. Traverse the string from right to left.
3. Find the first alphabetic character.
4. Convert it to lowercase.
5. Check whether it belongs to `"aeiouy"`.
6. Print:

   * `YES` if it is a vowel.
   * `NO` otherwise.

---

## Python 3 Solution

```python
question = input()

# Find the last letter
for char in reversed(question):
    if char.isalpha():
        last_letter = char.lower()
        break

if last_letter in "aeiouy":
    print("YES")
else:
    print("NO")
```

---

## Example

### Input

```text
Is it an apple?
```

### Output

```text
YES
```

The last letter is `e`, which is a vowel.

### Another Example

### Input

```text
Is it a melon?
```

### Output

```text
NO
```

The last letter is `n`, which is a consonant.

---

## Complexity Analysis

Let `n` be the length of the question.

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

---

## Key Concept

The important part of this problem is that the **last character is not necessarily the last letter**.

For example:

```text
Is it a banana ?
```

The last character before `?` is a space, but the last **letter** is `a`.

Since `a` is a vowel, the answer is:

```text
YES
```
