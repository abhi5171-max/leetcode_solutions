Problem Statement

Given a string s containing only the characters:

'(', ')', '{', '}', '[' and ']'

Determine whether the input string is valid.

A string is considered valid if:

Open brackets are closed by the same type of brackets.
Open brackets are closed in the correct order.
Every closing bracket has a corresponding opening bracket.
Examples
Example 1
Input: s = "()"
Output: true
Example 2
Input: s = "()[]{}"
Output: true
Example 3
Input: s = "(]"
Output: false
Example 4
Input: s = "([])"
Output: true
Example 5
Input: s = "([)]"
Output: false
Approach

This problem can be efficiently solved using a stack.

Algorithm
Create an empty stack.
Traverse each character in the string.
If the character is an opening bracket ((, {, [), push it onto the stack.
If the character is a closing bracket:
Check if the stack is empty.
Pop the top element from the stack.
Verify that it matches the corresponding opening bracket.
After processing all characters:
If the stack is empty, the string is valid.
Otherwise, it is invalid.

Complexity Analysis
Complexity	Value
Time	O(n)
Space	O(n)
Each character is processed once.
Each bracket is pushed and popped at most once.
Key Takeaway

A stack is the ideal data structure for handling nested and ordered bracket matching because it follows the Last In, First Out (LIFO) principle, which perfectly mirrors how opening and closing brackets must pair together.