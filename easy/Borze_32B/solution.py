s = input()

i = 0
result = []

while i < len(s):
    if s[i] == '.':
        result.append('0')
        i += 1
    elif s[i:i+2] == '-.':
        result.append('1')
        i += 2
    else:
        result.append('2')
        i += 2

print("".join(result))