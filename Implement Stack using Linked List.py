class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyStack:
    def __init__(self):
        self.top = None

    # Function to push an integer into the stack.
    def push(self, data):
        temp = Node(data)
        temp.next = self.top
        self.top = temp

    # Function to remove an item from top of the stack.
    def pop(self):
        # Add code here
        if self.top == None:
            return -1
        ans = self.top.data
        self.top = self.top.next
        return ans
        # Add code here


# {
#  Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = MyStack()
        q = int(input())
        q1 = list(map(int, input().split()))
        i = 0
        while (i < len(q1)):
            if (q1[i] == 1):
                s.push(q1[i + 1])
                i = i + 2
            elif (q1[i] == 2):
                print(s.pop(), end=" ")
                i = i + 1
            elif (s.isEmpty()):
                print(-1)
        print()

# } Driver Code Ends