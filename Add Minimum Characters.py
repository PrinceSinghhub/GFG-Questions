class Solution:
    def addMinChar (self, str1):
        if str1==str1[::-1]:
            return 0
        i=0
        j=len(str1)-1
        ans=j
        while i<=j:
            if str1[i]==str1[j]:
                i+=1
                j-=1
            else:
                ans-=1
                i=0
                j=ans
        return len(str1)-(ans+1)


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int (input ())
    for _ in range (t):
        str1 = input()

        ob = Solution()
        print(ob.addMinChar(str1))

# } Driver Code Ends