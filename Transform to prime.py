#User function Template for python3



class Solution:
    def minNumber(self, arr,n):
        # code here
        def checkPrime(N):
            if N>1:
                for i in range(2,int(N**0.5)+1):
                    if N%i==0:
                        return False
                return True
            else:
                return False
        i=0
        ans=sum(arr)
        while True:
            if checkPrime(ans+i):
               return i
            i+=1



#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
 #    l=list(map(int,input().split()))
 #    n=l[0]
 #    m=l[1]
    a=list(map(int,input().split()))
   # k = int(input())
  #  b = list(map(int, input().split()))
    ob = Solution()
    ans=ob.minNumber(a,n)
    print(ans)

# } Driver Code Ends