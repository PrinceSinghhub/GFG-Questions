#User function Template for python3

class Solution:
    
      def countSetBits(self,n):
      
       ans=0
       x=1
       
       while(x<=n):
           x=x*2
           quotient=(n+1)//x
           remainder=(n+1)%x
           total=quotient*(x//2)
           
           if remainder>(x//2):
               total+=remainder-x//2
           ans+=total
       return ans    
    #Function to return sum of count of set bits in the integers from 1 to n.
    # def countSetBits(self,n):
    #     add=0
    #     for i in range(1,n+1):
    #         add+=bin(i).count("1")
    #     return add

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        ob=Solution()
        print(ob.countSetBits(int(input())))
# } Driver Code Ends