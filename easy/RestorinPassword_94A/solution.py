encrypted = input().strip()

codes = {}

# Read codes for digits 0 to 9
for digit in range(10):
    code = input().strip()
    codes[code] = str(digit)

answer = []

# Each digit is represented by 10 bits
for i in range(0, 80, 10):
    chunk = encrypted[i:i + 10]
    answer.append(codes[chunk])

print("".join(answer))