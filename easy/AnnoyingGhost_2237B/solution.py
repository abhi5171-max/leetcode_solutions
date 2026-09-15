import sys
import bisect

input = sys.stdin.readline


class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, idx, value):
        idx += 1
        while idx <= self.n:
            self.bit[idx] += value
            idx += idx & -idx

    def sum(self, idx):
        """Number of active positions in [0, idx)."""
        result = 0
        while idx > 0:
            result += self.bit[idx]
            idx -= idx & -idx
        return result

    def kth(self, k):
        """
        Return the 0-based index of the k-th active position.
        k is 1-based.
        """
        idx = 0
        bit_mask = 1 << (self.n.bit_length() - 1)

        while bit_mask:
            nxt = idx + bit_mask
            if nxt <= self.n and self.bit[nxt] < k:
                idx = nxt
                k -= self.bit[nxt]
            bit_mask >>= 1

        return idx


def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())

        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        # (value, original position)
        elements = sorted((a[i], i) for i in range(n))

        # Fenwick tree stores which original positions are unused.
        bit = FenwickTree(n)

        for i in range(n):
            bit.add(i, 1)

        # Positions of elements whose value can already
        # be increased to the current target.
        candidates = []

        ptr = 0
        answer = 0

        for target in b:
            # Add every element that can reach this target.
            while ptr < n and elements[ptr][0] <= target:
                candidates.append(elements[ptr][1])
                ptr += 1

            # Remove positions that were already used.
            while candidates:
                pos = candidates[-1]

                # Check whether this position is still available.
                if bit.sum(pos + 1) - bit.sum(pos) == 1:
                    break

                candidates.pop()

            # No unused element can reach this target.
            if not candidates:
                answer = -1
                break

            # Choose the rightmost possible original position.
            pos = candidates.pop()

            # Number of unused elements before pos.
            swaps = bit.sum(pos)

            answer += swaps

            # Mark this position as used.
            bit.add(pos, -1)

        print(answer)


if __name__ == "__main__":
    solve()
