months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

current = input().strip()
k = int(input())

current_index = months.index(current)
new_index = (current_index + k) % 12

print(months[new_index])