#User function Template for python3

class Solution:
   def solve(self, arr, n):
       arr.sort()
       d=d1=0
       s=s1=""
       for i in range(n):
           if(i%2==0):
               #s=s+str(arr[i])
               d=d*10 +arr[i]
           else:
               #s1=s1+str(arr[i])
               d1=d1*10 +arr[i]
       #if(s1==""):
          # return int(s)
       #if(s==""):
        #   return int(s1)
        
       return d+d1 

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.solve(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends