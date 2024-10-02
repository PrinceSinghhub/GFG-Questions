#User function Template for python3

class Solution:
    def count (self,s):
        
        u = 0
        l = 0
        nm = 0
        sp = 0
        for i in s:
            if i.isupper():
                u+=1
            elif i.islower():
                l+=1
            
            elif i.isdigit():
                nm+=1
            
            else:
                sp+=1
        
        return [u,l,nm,sp]
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    res = ob.count (s)
    
    for i in res:
        print (i)
    
# Contributed By: Pranay Bansal

# } Driver Code Ends