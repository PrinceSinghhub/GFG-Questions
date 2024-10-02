import math


class Solution:

    # Function to count number of pairs such that x^y is greater than y^x.
    def countPairs(self, arr, brr):
        for i in range(len(arr)):
            arr[i] = math.log(arr[i]) / arr[i]
        for i in range(len(brr)):
            brr[i] = math.log(brr[i]) / brr[i]
        arr.sort()
        brr.sort()
        cnt = 0
        for i in range(len(arr)):
            idx = bisect.bisect_left(brr, arr[i])
            cnt += idx
        return cnt