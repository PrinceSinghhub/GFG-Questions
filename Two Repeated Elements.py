class Solution:

    # Function to find two repeated elements.
    def twoRepeated(self, a, n):

        dp = [0] * (n + 3);
        count = 0
        ans = []
        for i in range(len(a)):
            dp[a[i]] += 1;
            if (count == 2):
                break;
            if (a[i] < n + 1 and dp[a[i]] == 2):
                ans.append(a[i]);
                count += 1;

        return ans


# {
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        N = int(input())

        A = [int(x) for x in input().strip().split()]

        obj = Solution()
        ans = obj.twoRepeated(A, N)
        print(ans[0], ans[1])

        T -= 1


if __name__ == "__main__":
    main()