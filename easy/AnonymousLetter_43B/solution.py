from collections import Counter
 
heading = input()
text = input()
 
count = Counter()
 
for ch in heading:
    if ch != ' ':
        count[ch] += 1
 
for ch in text:
    if ch == ' ':
        continue
    if count[ch] == 0:
        print("NO")
        break
    count[ch] -= 1
else:
    print("YES")
