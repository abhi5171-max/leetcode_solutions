n = int(input())

alcohol = {
    "ABSINTH", "BEER", "BRANDY", "CHAMPAGNE", "GIN",
    "RUM", "SAKE", "TEQUILA", "VODKA", "WHISKEY", "WINE"
}

count = 0

for _ in range(n):
    s = input()
    
    if s.isdigit():
        if int(s) < 18:
            count += 1
    else:
        if s in alcohol:
            count += 1

print(count)