guest = input()
host = input()
pile = input()

required = guest + host

if sorted(required) == sorted(pile):
    print("YES")
else:
    print("NO")