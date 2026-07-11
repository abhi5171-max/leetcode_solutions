s = input()
n = int(input())

ans = None

for _ in range(n):
    page = input()
    if page.startswith(s):
        if ans is None or page < ans:
            ans = page

print(ans if ans is not None else s)