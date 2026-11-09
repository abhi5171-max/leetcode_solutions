t = int(input())

for _ in range(t):
    n = int(input())
    a = input()

    m = int(input())
    b = input()
    c = input()

    left = ""
    right = ""

    for i in range(m):
        if c[i] == 'V':
            left = b[i] + left
        else:
            right += b[i]

    print(left + a + right)