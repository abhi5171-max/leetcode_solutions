a, c = map(int, input().split())

b = 0
place = 1

while a > 0 or c > 0:
    da = a % 3
    dc = c % 3

    db = (dc - da) % 3
    b += db * place

    a //= 3
    c //= 3
    place *= 3