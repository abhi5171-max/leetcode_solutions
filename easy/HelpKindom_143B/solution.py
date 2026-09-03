s = input().strip()

# Check whether the original number is negative
negative = s.startswith('-')

# Remove the minus sign
if negative:
    s = s[1:]

# Split integer and fractional parts
if '.' in s:
    integer_part, fraction_part = s.split('.')
else:
    integer_part = s
    fraction_part = ''

# Format integer part with commas
integer_part = f"{int(integer_part):,}"

# Keep exactly two fractional digits
fraction_part = (fraction_part + "00")[:2]

# Build the financial format
result = f"${integer_part}.{fraction_part}"

# Add parentheses for negative numbers
if negative:
    result = f"({result})"

print(result)