n = input()
 
count = sum(1 for ch in n if ch in ('4', '7'))
 
if count > 0 and all(d in ('4', '7') for d in str(count)):
    print("YES")
else:
    print("NO")
