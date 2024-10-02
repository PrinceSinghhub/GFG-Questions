#User function Template for python3

from typing import List

class Solution:
    def reverse(self,st): 
        
        stack = []
        
        while st:
            stack.append(st.pop())
        
        return stack
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            ans=(ob.reverse(arr))
            for el in ans:
                print(el,end=" ")
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends