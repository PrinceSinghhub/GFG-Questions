# User function Template for python3

class Solution:

    # Function to delete middle element of a stack.
    def deleteMid(self, s, sizeOfStack):
        mid = (sizeOfStack - 1) // 2

        s.pop(mid)


# {
#  Driver Code Starts
# Initial Template for Python 3

def main():
    t = int(input())
    while (t > 0):
        sizeOfStack = int(input())
        myStack = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.deleteMid(myStack, sizeOfStack)
        while (len(myStack) > 0):
            print(myStack[-1], end=" ")
            myStack.pop()
        print()
        t -= 1