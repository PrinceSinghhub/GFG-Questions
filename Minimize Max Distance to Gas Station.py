# {
# Driver Code Starts
# Initial Template for Python 3


# } Driver Code Ends
# User function Template for python3

from math import floor


class Solution:
    def isValid(self, stations, K, distance, n):
        new_stations = 0
        for i in range(1, n):
            new_stations += floor((stations[i] - stations[i - 1]) / distance)

        return new_stations <= K

    def findSmallestMaxDist(self, stations, K):
        n = len(stations)
        start = 0.0
        end = stations[-1] - stations[0]

        while end - start > 1e-6:
            mid = start + (end - start) / 2.0
            if self.isValid(stations, K, mid, n):
                end = mid
            else:
                start = mid

        return start + 0.000001


# {
# Driver Code Starts.
import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        stations = list(map(int, input().split()))
        K = int(input())
        ob = Solution()
        print('%.2f' % ob.findSmallestMaxDist(stations, K))
# } Driver Code Ends