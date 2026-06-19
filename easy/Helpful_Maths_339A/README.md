Problem Statement

Xenia is learning addition and can only calculate sums when the numbers are arranged in non-decreasing order. Given a sum consisting only of numbers 1, 2, and 3 separated by +, rearrange the numbers so that they appear in sorted order.

Example

Input

3+2+1

Output

1+2+3
Approach
Split the input string using '+' as the delimiter.
Sort the resulting list of numbers.
Join the sorted numbers back together using '+'.
Print the result.
Python Solution
s = input()

nums = s.split('+')
nums.sort()

print('+'.join(nums))
Complexity Analysis
Time Complexity: O(n log n) (sorting the numbers)
Space Complexity: O(n) (storing the numbers in a list)
Key Concepts Learned
String manipulation with split()
Sorting lists using sort()
Combining strings with join()
Greedy thinking through ordering elements