#User function Template for python3

class Solution:
    def minLength(self, s, n):

        l=list(s)

        d={}

        for i in range(1,10,2):

            d[str(i)]=str((i+1)%10)

            d[str((i+1)%10)]=str(i)

        i=0

        while(i<n-1 and n>1):

            if d[l[i]]==l[i+1]:

                l.pop(i)

                l.pop(i)

                n=n-2

                if i!=0:

                    i-=1

            else:

                i+=1

        return len(l)


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        ob = Solution()
        print(ob.minLength(s,n))
# } Driver Code Ends