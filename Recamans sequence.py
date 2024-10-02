#User function Template for python3

class Solution:
    def recamanSequence(self, n):

        # code here

        ans = [0]

        self.helper(n, ans)

        return ans

    def helper(self, n, ans):

        if n==0:

            return

        self.helper(n-1, ans)

        if (ans[n-1]-n > 0) and (ans[n-1]-n) not in ans:

            ans.append(ans[n-1]-n)

        else:

            ans.append(ans[n-1]+n)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.recamanSequence(n)
        for i in range(n):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends