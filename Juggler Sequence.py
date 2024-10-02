# User function Template for python3

class Solution:
    def jugglerSequence(self, N):

        # code here

        ans = []

        self.helper(N, ans)

        return ans

    def helper(self, num, ans):

        ans.append(num)

        if num == 1:
            return ans

        if num % 2 == 0:

            num = int(pow(num, 0.5))

        else:

            num = int(pow(num, 1.5))

        return self.helper(num, ans)


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        arr = ob.jugglerSequence(N)
        for i in (arr):
            print(i, end=" ")
        print()
# } Driver Code Ends