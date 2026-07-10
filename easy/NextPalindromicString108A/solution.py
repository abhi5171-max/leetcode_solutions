h, m = map(int, input().split(":"))

while True:
    m += 1
    if m == 60:
        m = 0
        h = (h + 1) % 24

    time = f"{h:02d}{m:02d}"
    if time == time[::-1]:
        print(f"{h:02d}:{m:02d}")
        break