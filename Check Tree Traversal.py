#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def checktree(self, preorder, inorder, postorder, N): 
        # Your code goes here
        if N==0:return True
        if N==1 :
            return preorder[0]==postorder[0] and postorder[0]==inorder[0] 
        root=preorder[0]
        if root!=postorder[N-1]:return False
        if root not in set(inorder):
            return False
        else:
            rooti=inorder.index(root)
            leftN=rooti
            rightN=N-rooti-1
            return self.checktree(preorder[1:leftN+1],inorder[:rooti],postorder[:leftN],leftN) and \
                  self.checktree(preorder[leftN+1:],inorder[rooti+1:],postorder[leftN:N-1],rightN)

#{ 
 # Driver Code Starts.

# Driver Code 
if __name__ == "__main__": 
	t = int(input())
	for _ in range(t):
		n = int(input())
		preorder = list(map(int, input().strip().split()))
		inorder = list(map(int, input().strip().split()))
		postorder = list(map(int, input().strip().split()))
		obj = Solution()
		if(obj.checktree(preorder, inorder, postorder, n)):
			print("Yes") 
		else: 
			print("No") 


# } Driver Code Ends