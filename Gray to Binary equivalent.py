class Solution:
    def grayToBinary(self, n):
        from collections import deque
        from functools import reduce

        q = deque()
        while n > 0:
            q.appendleft(n % 2)
            n //= 2

        bits = []
        for b in q:
            if not bits:
                bits.append(b)
            else:
                bits.append(bits[-1] ^ b)
        return reduce(lambda v, e: v * 2 + e, bits, 0)


# {
# Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):
        n = int(input())
        ob = Solution()
        print(ob.grayToBinary(n))
        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends