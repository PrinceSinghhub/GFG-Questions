#User function Template for python3
import math
class Solution:
    def rectangleCount(self, A):
       k=int(math.sqrt(A))
       c=0
       for l in range(1,k+1):
          if(A%l==0):
               if((l+(A//l))%2!=0):
                   c+=1
               elif(l%2!=0 and (A//l)%2!=0):
                   c+=1
               elif(l%2==0 and (A//l)==l):
                  c+=1
       return c   


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A = int(input())
        
        ob = Solution()
        print(ob.rectangleCount(A))
# } Driver Code Ends