def _push(arr):
   stack = []
   for i in arr:
       stack.append(i)
   return stack


#_pop function to print elements of the stack remove as well
def _pop(stack):
       while(len(stack) > 0):
           print(stack.pop(),end = " ")



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr=[int(i) for i in input().split()]
        stack = _push(arr)
        _pop(stack)
        print()

# } Driver Code Ends