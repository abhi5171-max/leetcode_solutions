s = input().lower()

vowels = "aoyeui"
result = ""

for ch in s:
    if ch not in vowels:
        result += "." + ch

print(result)