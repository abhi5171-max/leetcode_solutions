s = input().strip()

result = []
max_char = ''

for ch in reversed(s):
    if not max_char or ch >= max_char:
        result.append(ch)
        max_char = ch

print(''.join(reversed(result)))