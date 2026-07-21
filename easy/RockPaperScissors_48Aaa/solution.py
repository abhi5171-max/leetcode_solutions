f = input().strip()
m = input().strip()
s = input().strip()

beats = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}

# All same
if f == m == s:
    print("?")

# All different
elif len({f, m, s}) == 3:
    print("?")

# Exactly two are same
else:
    if f == m:
        common = f
        unique = s
        winner = "S"
    elif f == s:
        common = f
        unique = m
        winner = "M"
    else:
        common = m
        unique = f
        winner = "F"

    if beats[unique] == common:
        print(winner)
    else:
        print("?")