word = input()

if word.isupper() or (word[0].islower() and word[1:].isupper()):
    print(word.swapcase())
else:
    print(word)