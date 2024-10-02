# User function Template for python3

class Solution:
    def minPartition(self, N):

        # code here

        arr = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

        l = []

        for x in arr:

            while N >= x and N > 0:
                N -= x

                l.append(x)

        return l


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        arr = ob.minPartition(N)
        for i in range(len(arr)):
            print(arr[i], end=" ")
        print()
# } Driver Code Ends