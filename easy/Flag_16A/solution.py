n, m = map(int, input().split())
flag = [input().strip() for _ in range(n)]
 
for i in range(n):
    # Check if all characters in the row are the same
    if any(flag[i][j] != flag[i][0] for j in range(1, m)):
        print("NO")
        exit()
 
    # Check if adjacent rows have different colors
    if i > 0 and flag[i][0] == flag[i - 1][0]:
        print("NO")
        exit()
 
print("YES")
