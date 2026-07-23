n = int(input())

rats = []
women_children = []
men = []
captain = []

for _ in range(n):
    name, status = input().split()

    if status == "rat":
        rats.append(name)
    elif status == "woman" or status == "child":
        women_children.append(name)
    elif status == "man":
        men.append(name)
    else:
        captain.append(name)

for person in rats:
    print(person)
for person in women_children:
    print(person)
for person in men:
    print(person)
for person in captain:
    print(person)