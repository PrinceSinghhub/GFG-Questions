#User function Template for python3



class Solution:
    def rearrangeArray(self, arr, n):

        # code here

        result = []

        arr.sort()

        left = 0

        right = n-1

        while left < right:

            result.append(arr[left])

            result.append(arr[right])

            left += 1

            right -= 1

        if n%2 == 1:

            result.append(arr[left])

        for i in range(0, n):

            arr[i] = result[i]


#{
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input().strip())
        arr = list(map(int, input().strip().split()))
        Solution().rearrangeArray(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends