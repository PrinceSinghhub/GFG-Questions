#User function Template for python3
class Solution:
    def leafNodes(self, arr, N):

        if len(arr)==0:

            return []

        if len(arr)==1:

            return [arr[0]]

        for i in range(1,len(arr)):

            if arr[i]>arr[0]:

                idx=i

                break

        else:

            idx=i+1

        left=self.leafNodes(arr[1:idx],len(arr[1:idx]))

        right=self.leafNodes(arr[idx:],len(arr[idx:]))

        return left+right



#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        ob = Solution()
        ans = ob.leafNodes(arr,N)
        for i in range(len(ans)):
            print(ans[i], end = " ")
        print()
# } Driver Code Ends