# 🚢 A. Sinking Ship

## Problem Overview

A sinking ship must evacuate its crew following a strict priority:

1. Rats
2. Women and Children (same priority)
3. Men
4. Captain (always last)

If two crew members belong to the same priority group, they leave in the same order they originally stood in line.

The goal is to print the evacuation order.

## Approach

* Create four separate lists:

  * `rats`
  * `women_children`
  * `men`
  * `captain`
* Read each crew member and place their name into the appropriate list.
* Finally, print the lists in the required priority order.
* Since names are appended while reading the input, the original order within each category is preserved automatically.

## Algorithm

1. Read `n`.
2. Initialize four empty lists.
3. For each crew member:

   * Read the name and status.
   * Add the name to the corresponding list.
4. Print:

   * Rats
   * Women and Children
   * Men
   * Captain

## Complexity Analysis

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

## Key Concepts

* Arrays (Lists)
* Simulation
* Categorization
* Order preservation

## Python Solution

```python
n = int(input())

rats = []
women_children = []
men = []
captain = []

for _ in range(n):
    name, status = input().split()

    if status == "rat":
        rats.append(name)
    elif status == "woman" or status == "child":
        women_children.append(name)
    elif status == "man":
        men.append(name)
    else:
        captain.append(name)

for person in rats:
    print(person)
for person in women_children:
    print(person)
for person in men:
    print(person)
for person in captain:
    print(person)
```
