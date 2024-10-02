# User function Template for python3

import  collections
class Solution:

    # Function to find all elements in array that appear more than n/k times.
    def countOccurence(self, arr, n, k):
        # agg = collections.Counter(arr)


        tar = n // k
        count = 0

        temp = list(set(arr))

        for i in temp:
            if arr.count(i) > tar:
                count += 1

        return count


ans = Solution()
arr = [3,1,2,2,1,2,3,3]
k = 4
N = len(arr)
print(ans.countOccurence(arr,N,k))