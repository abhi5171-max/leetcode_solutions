n, p1, p2, p3, t1, t2 = map(int, input().split())

intervals = [tuple(map(int, input().split())) for _ in range(n)]

power = 0

for i in range(n):
    l, r = intervals[i]

    # Power consumed while Tom is actively using the laptop
    power += (r - l) * p1

    # Idle time before the next working interval
    if i < n - 1:
        gap = intervals[i + 1][0] - r

        # Normal mode
        normal = min(gap, t1)
        power += normal * p1
        gap -= normal

        # Screensaver mode
        screen = min(gap, t2)
        power += screen * p2
        gap -= screen

        # Sleep mode
        power += gap * p3

print(power)