vowels = set("aeiou")
required = [5, 7, 5]

for i in range(3):
    line = input()
    count = sum(1 for ch in line if ch in vowels)

    if count != required[i]:
        print("NO")
        break
else:
    print("YES")