# Function to find maximum
# product subarray
def maxProduct(self, arr, n):
    # code here

    ans = maxsum = currentsum = arr[0]

    for i in arr[1::]:
        if i < 0:
            maxsum, currentsum = currentsum, maxsum
        maxsum = max(i, i * maxsum)
        currentsum = min(i, i * currentsum)

        ans = max(ans, maxsum)
    return ans


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends