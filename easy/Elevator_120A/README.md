# 120A - Elevator

## Problem Statement
A VIP enters an elevator through either the **front** or **back** door and holds one of the two rails. Since people always hold the rail with their strongest hand, determine whether the VIP is **left-handed** or **right-handed**.

## Approach
- If the person enters from the **front**:
  - Rail **1** → Left hand (`L`)
  - Rail **2** → Right hand (`R`)
- If the person enters from the **back**:
  - Rail **1** → Right hand (`R`)
  - Rail **2** → Left hand (`L`)

Use simple conditional statements to determine the answer.

## Algorithm
1. Read the entrance door (`front` or `back`).
2. Read the rail number.
3. If:
   - (`front` and rail `1`) OR (`back` and rail `2`) → Print `L`
4. Otherwise print `R`.

## Complexity Analysis
- **Time Complexity:** `O(1)`
- **Space Complexity:** `O(1)`

## Python Solution

with open("input.txt", "r") as fin:
    door = fin.readline().strip()
    rail = int(fin.readline())

with open("output.txt", "w") as fout:
    if (door == "front" and rail == 1) or (door == "back" and rail == 2):
        fout.write("L")
    else:
        fout.write("R")

## Key Concepts
- Conditional Statements
- Simulation