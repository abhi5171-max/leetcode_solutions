n = input().strip()
m = input().strip()

# Check if both numbers contain the same digits
if sorted(n) != sorted(m):
    print("WRONG_ANSWER")
else:
    digits = sorted(n)

    # If all digits are zero
    if digits[-1] == '0':
        smallest = "0"
    else:
        # Place the first non-zero digit first
        smallest = ""
        for i, d in enumerate(digits):
            if d != '0':
                smallest = d
                digits.pop(i)
                break
        smallest += "".join(digits)

    if m == smallest:
        print("OK")
    else:
        print("WRONG_ANSWER")