# # def sum(n):
    
# #     # base condition
# #     if n == 1:
# #         return 1
    
# #     return n + sum(n - 1)

# # if __name__ == "__main__":
# #     n = 5
# #     print(sum(n))
    
# # # 5  + 4 + 3 + 2 + 1 

# # Python code to implement Fibonacci series

# # # Function for fibonacci
# # def fib(n):

# #     # Stop condition
# #     if (n == 0):
# #         return 0

# #     # Stop condition
# #     if (n == 1 or n == 2):
# #         return 1

# #     # Recursion function
# #     else:
# #         return (fib(n - 1) + fib(n - 2))


# # # Driver Code

# # # Initialize variable n.
# # n = 5
# # print("Fibonacci series of 5 numbers is :",end=" ")

# # # for loop to print the fibonacci series.
# # for i in range(0,n): 
# #     print(fib(i),end=" ")

# # Assume that n is greater than or equal to 1 */
# # def fun1(n):
# #     if(n == 1):
# #         return 0
# #     else:
# #         return 1 + fun1(n//2)

# # # Driver code
# # print(fun1(8))

# s = input().strip()

# #check for negtivity
# negative = s.startswith('-')

# #remove minus
# if negative:
#   s = s[1:]
 
# #seperate the s 
# if '.' in s:
#   integer_part, fraction_part = s.split('.')
# else:
#   integer_part = s
#   fraction_part = ""
  
# #format integer
# integer_part = f"{int(integer_part):,}"

# #format fraction
# fraction_part = (fraction_part + "00")[:2]

# #present
# result = f"${integer_part}.{fraction_part}"

# #negativity
# if negative:
#   result = f"{(result)}"
  
# print(result)

n = int(input())
pos = [0] * (n + 1)
print(pos)