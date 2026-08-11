import sys
from itertools import permutations


def main():
    p = list(map(int, sys.stdin.readline().split()))

    p1, p2, p3, p4, a, b = p
    nums = [p1, p2, p3, p4]

    perms = list(permutations(nums))

    answer = 0

    for x in range(a, b + 1):
        count = 0

        for perm in perms:
            value = x

            for mod in perm:
                value %= mod

            if value == x:
                count += 1

        if count >= 7:
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()