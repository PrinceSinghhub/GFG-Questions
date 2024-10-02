# User function Template for python3

class Solution:
    def splitArray(self, arr, N, K):

        # code here

        def isValid(limit, k):

            cnt = 0

            currSum = 0

            for num in arr:

                currSum += num

                if currSum > limit:
                    cnt += 1

                    currSum = num

            return cnt + 1 <= k

        sm = sum(arr)

        lo, hi = max(arr), sm

        ans = 0

        while lo <= hi:

            mid = (lo + hi) // 2

            # print(lo, hi, mid)

            if isValid(mid, K):

                ans = mid

                hi = mid - 1

            else:
                lo = mid + 1

        return ans
        # code here
