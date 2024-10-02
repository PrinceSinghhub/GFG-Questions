# User function Template for python3

class Solution:
    def isRepresentingBST(self, arr, N):

        copy = [i for i in arr]

        copy = list(set(copy))

        if len(copy) < len(arr):
            return 0

        copy.sort()

        if copy == arr:
            return 1

        return 0


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])

        ob = Solution()
        print(ob.isRepresentingBST(arr, N))
# } Driver Code Ends