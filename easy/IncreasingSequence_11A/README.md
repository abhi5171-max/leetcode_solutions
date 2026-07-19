A. Increasing Sequence
📌 Problem

Given a sequence of integers and a positive integer d, you can repeatedly choose any element and increase it by d in one move. Determine the minimum number of moves required to make the sequence strictly increasing.

💡 Approach
Traverse the array from left to right.
If the current element is already greater than the previous one, no action is needed.
Otherwise, calculate the minimum number of additions of d required to make it strictly greater than the previous element.
Update the current element and add the number of operations to the answer.
✅ Algorithm
Read n, d, and the sequence.
Iterate from the second element to the last.
If a[i] <= a[i-1]:
Compute the required increment.
Find the minimum number of operations using ceiling division.
Update the element and the operation count.
Print the total number of operations.
⏱️ Complexity
Time Complexity: O(n)
Space Complexity: O(1) (excluding the input array)
🛠️ Concepts Used
Greedy Algorithm
Mathematics
Ceiling Division
Array Traversal
Simulation