class Solution:

    def beautySum(self, s):

        # Code here

        beauty,sum=0,0

        for i in range (len(s)):

            ch={}

            for j in range (i,len(s)):

                ch.setdefault(s[j],0)

                ch[s[j]]+=1

                beauty+=max(ch.values())-min(ch.values())

        return beauty


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        print(ob.beautySum(s))
# } Driver Code Ends