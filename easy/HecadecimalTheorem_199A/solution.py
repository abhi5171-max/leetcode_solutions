n = int(input())

# Generate Fibonacci numbers up to n
fib = [0, 1]

while fib[-1] + fib[-2] <= n:
    fib.append(fib[-1] + fib[-2])

# Try every possible pair
for a in fib:
    for b in fib:
        c = n - a - b

        if c in fib:
            print(a, b, c)
            exit()

print("I'm too stupid to solve this problem")