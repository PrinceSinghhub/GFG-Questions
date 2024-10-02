from itertools import product

MOD = 1000000007


def numOfWays(M, N):
    DIR = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
    cannot_place = 0
    for r, c in product(range(M), range(N)):
        for dr, dc in DIR:

            row, col = r + dr, c + dc

            if 0 <= row < M and 0 <= col < N:
                cannot_place += 1

    total_ways = M * N

    return (total_ways * (total_ways - 1) - cannot_place) % MOD


# {
# Driver Code Starts
# Initial Template for Python 3

import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m, n = map(int, input().strip().split())
        print(numOfWays(m, n))

# } Driver Code Ends