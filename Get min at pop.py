# User function Template for python3

# Function to push all the elements into the stack.
def _push(a, n):
    stack = a
    return stack


# Function to print minimum value in stack each time while popping.
def _getMinAtPop(stack):
    for i in range(len(stack)):
        Min = min(stack)
        stack.pop()
        print(Min, end=" ")

    # code here