# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
from typing import List

import math


class Solution:
    def kthPermutation(self, n: int, k: int) -> str:
        # code here
        digits = [i for i in range(1, n + 1)]
        ans = ""
        k -= 1
        for i in range(n):
            ans += str(digits.pop(k // math.factorial(n - 1 - i)))
            k -= math.factorial(n - 1 - i) * (k // math.factorial(n - i - 1))
        return ans


# {
# Driver Code Starts.
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N, K = map(int, input().split())

        obj = Solution()
        res = obj.kthPermutation(N, K)

        print(res)

# } Driver Code Ends