class Solution:
    # Function to return maximum sum subarray by removing at most one element.
    def maxSumSubarray(self, arr, n):
        fw = [0 for k in range(n)]
        bw = [0 for k in range(n)]

        # Initialize current max and max so far.
        cur_max, max_so_far = arr[0], arr[0]
        fw[0] = cur_max

        # calculating maximum sum subarrays in forward
        # direction
        for i in range(1, n):
            cur_max = max(arr[i], cur_max + arr[i])
            max_so_far = max(max_so_far, cur_max)

            # storing current maximum till ith, in
            # forward array
            fw[i] = cur_max

        # calculating maximum sum subarrays in backward
        # direction
        cur_max = max_so_far = bw[n - 1] = arr[n - 1]
        i = n - 2
        while i >= 0:
            cur_max = max(arr[i], cur_max + arr[i])
            max_so_far = max(max_so_far, cur_max)

            # storing current maximum from ith, in
            # backward array
            bw[i] = cur_max
            i -= 1

        #  Initializing final ans by max_so_far so that,
        #  case when no element is removed to get max sum
        #  subarray is also handled
        fans = max_so_far

        #  choosing maximum ignoring ith element
        for i in range(1, n - 1):
            fans = max(fans, fw[i - 1] + bw[i + 1])

        return fans


# {
#  Driver Code Starts
# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(Solution().maxSumSubarray(arr, n))