s = input().strip()

integer_part, fractional_part = s.split('.')

# If integer part ends with 9, carrying is not allowed
if integer_part[-1] == '9':
    print("GOTO Vasilisa.")
else:
    # Fractional part >= 0.5
    if fractional_part[0] >= '5':
        last_digit = int(integer_part[-1])
        integer_part = integer_part[:-1] + str(last_digit + 1)

    print(integer_part.lstrip('0') or '0')