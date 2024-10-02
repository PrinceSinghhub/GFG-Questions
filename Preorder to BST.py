# User function Template for python3

class Node:

    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None


def post_order(pre, size):
    if not size:
        return

    root = Node(pre[0])
    stack = [root]

    for i in range(1, size):
        curr = stack[len(stack) - 1]

        if (pre[i] <= curr.data):
            curr.left = Node(pre[i])
            stack.append(curr.left)
        else:
            while stack and pre[i] > stack[len(stack) - 1].data:
                curr = stack.pop()
            curr.right = Node(pre[i])
            stack.append(curr.right)
    return root


# {
# Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None


def postOrd(root):
    if not root:
        return
    postOrd(root.left)
    postOrd(root.right)
    print(root.data, end=' ')


if __name__ == '__main__':
    t = int(input())

    for _tcs in range(t):
        size = int(input())
        pre = [int(x) for x in input().split()]

        root = post_order(pre, size)

        postOrd(root)
        print()
# } Driver Code Ends
