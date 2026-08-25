n = int(input())
ticket = input().strip()

# Check if all digits are lucky
if not all(ch in '47' for ch in ticket):
    print("NO")
else:
    half = n // 2

    first_sum = sum(int(ch) for ch in ticket[:half])
    second_sum = sum(int(ch) for ch in ticket[half:])

    if first_sum == second_sum:
        print("YES")
    else:
        print("NO")