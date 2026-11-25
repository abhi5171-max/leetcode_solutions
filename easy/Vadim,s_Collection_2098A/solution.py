
t = int(input())

for _ in range(t):
    s = input().strip()

    digits = sorted(s)
    ans = []

    for i in range(10):
        required = 9 - i

        for j in range(len(digits)):
            if int(digits[j]) >= required:
                ans.append(digits.pop(j))
                break

    print("".join(ans))
