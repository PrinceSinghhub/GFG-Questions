class Solution:
    def findSum(self, X, Y):
        # code here

        return int(X) + int(Y)


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        x = input()
        y = input()
        ob = Solution()
        answer = ob.findSum(x, y)

        print(answer)