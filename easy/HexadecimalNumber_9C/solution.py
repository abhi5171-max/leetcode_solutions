n = int(input())

count = 0

def dfs(x):
    global count
    if x > n:
        return
    count += 1
    dfs(x * 10)
    dfs(x * 10 + 1)

dfs(1)

print(count)