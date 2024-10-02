class Solution:
    # Function to find triplets with zero sum.
    def findTriplets(self, arr, n):

        arr.sort()
        for i in range(n):
            low = i + 1
            high = n - 1

            while low < high:
                if arr[low] + arr[high] < -arr[i]:
                    low += 1

                elif arr[low] + arr[high] > -arr[i]:
                    high -= 1

                else:
                    return True

        return False


ans = Solution()
n = 5
arr = [0, -1, 2, -3, 1]
print(ans.findTriplets(arr,n))