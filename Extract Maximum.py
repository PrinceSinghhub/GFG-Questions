#User function Template for python3

class Solution:
    def extractMaximum(self,S): 
        # code here
        #if no number in S return -1
        if S.isalpha():
            return -1
        
        #replce alpha to space in S    
        for i in S:
            if i.isalpha():
                S = S.replace(i," ")
        #split S to list
        S = S.split()
        
        #check for the max number
        count = 0
        for j in S:
            if int(j) > count:
                count = int(j)
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        S = input()
        ob = Solution()
        print(ob.extractMaximum(S)) 

# } Driver Code Ends