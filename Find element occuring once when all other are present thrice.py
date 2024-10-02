class Solution:
    def singleElement(self, arr, N):

        mydata = {}
        for i in arr:
            if i in mydata:
                mydata[i] += 1
            else:
                mydata[i] = 1

        for i in mydata:
            if mydata[i] == 1:
                return i
        # code here


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = list(map(int, input().split()))

        ob = Solution()
        print(ob.singleElement(arr, N))