2. Elephant (617A)

An elephant starts at position 0 and wants to reach position x. In one move, it can advance by 1, 2, 3, 4, or 5 units. Find the minimum number of moves required.

Approach
Since the elephant can move up to 5 units in one step, always taking the maximum possible step minimizes the total number of moves.

The answer is simply:

ceil(x / 5)

In integer arithmetic:

(x + 4) // 5

Time Complexity
O(1)
Space Complexity
O(1)
Key Learnings