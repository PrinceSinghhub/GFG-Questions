class Solution:

    def minOperation(self, s):

        #code here

        big = ''

        s1=''

        for x in range(len(s)):

            s1+=s[x]

            if s1 in s[x+1:]:

                big = s1

        if big:return len(s)-len(big)+1

        return len(s)

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.minOperation(s)
        print(ans)
# } Driver Code Ends