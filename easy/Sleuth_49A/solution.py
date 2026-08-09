question = input()

# Find the last letter
for char in reversed(question):
    if char.isalpha():
        last_letter = char.lower()
        break

if last_letter in "aeiouy":
    print("YES")
else:
    print("NO")