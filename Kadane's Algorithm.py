class Solution:
    def maxSubArraySum(self, arr, N):

        result = True
        for i in arr:
            if i > 0:
                result = False
                break

        if result == True:
            return max(arr)

        else:

            maxsum = 0
            currentsum = 0

            for i in arr:
                currentsum += i
                if currentsum > maxsum:
                    maxsum = currentsum

                if currentsum < 0:
                    currentsum = 0

            return maxsum