n = int(input())
a = list(map(int, input().split()))
 
count = [0, 0, 0, 0]
 
for x in a:
    count[x] += 1
 
print(n - max(count[1], count[2], count[3]))