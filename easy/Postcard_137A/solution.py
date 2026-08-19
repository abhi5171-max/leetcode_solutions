s = input().strip()

answer = 0
count = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        answer += (count + 4) // 5
        count = 1

# Process the final group
answer += (count + 4) // 5

print(answer)