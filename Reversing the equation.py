class Solution:

    def reverseEqn(self, s):

        s1=''

        l=list(s)

        l1=['+','-','*','/']

    

        s2=''

        s3=''

        while l:

            a=l.pop()

            if a in l1:

                s3+=s2[::-1]

                s3+=a

                s2=''

                

            else:

                s2+=a

        s3+=s2[::-1]

        return s3


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseEqn(s)
        print(ans)
# } Driver Code Ends