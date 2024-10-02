class Solution:
    def thirdLargest(self, a, n):
        # code here

        if n < 3:
            return -1

        if n == 3:
            a.sort()
            return a[0]

        else:

            a.sort()

            return a[-3]


# {
#  Driver Code Starts
# Your code goes here
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(Solution().thirdLargest(arr, n))
# } Driver Code Ends