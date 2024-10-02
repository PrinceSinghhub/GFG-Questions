# Your task is to complete all these function's
# function should append an element on to the stack
def push(arr, ele):
    # Code here
    
    arr.append(ele)

# Function should pop an element from stack
def pop(arr):
    arr.pop()
    # Code here

# function should return 1/0 or True/False
def isFull(n, arr):
    if len(arr) == n:
        return True
    return False

# function should return 1/0 or True/False
def isEmpty(arr):
    
    if len(arr) == 0:
        return True
    return False
    #Code here

# function should return minimum element from the stack
def getMin(n, arr):
    
    min = 10**9
    
    for i in arr:
        if i < min:
            min = i
    return min
    # Code here


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        stack = []
        while(not isEmpty(stack)):
            pop(stack)
            
        for i in range(n):
            push(stack, arr[i])
        print(getMin(n, stack))
# contributed by: Harshit Sidhwa

# } Driver Code Ends