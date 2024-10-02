# User function Template for python3
class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def constructBinaryTree(self, pre, preMirror, size):

        def buildACompleetTree(pre, mirror):
            if not pre and not mirror:
                return None
            n = TreeNode(pre[0])
            if len(pre) == 1:
                return n

            pre = pre[1:]
            mirror = mirror[1:]
            i, j = pre.index(mirror[0]), mirror.index(pre[0])
            n.left = buildACompleetTree(pre[:i], mirror[j:])
            n.right = buildACompleetTree(pre[i:], mirror[:j])
            return n

        return buildACompleetTree(pre, preMirror)


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':

    def printInorder(node):
        if node == None:
            return
        printInorder(node.left)
        print(node.data, end=" ")
        printInorder(node.right)


    test_cases = int(input())
    for _ in range(test_cases):
        N = int(input())
        pre = list(map(int, input().split()))
        preMirror = list(map(int, input().split()))
        res = Solution().constructBinaryTree(pre, preMirror, N)
        if printInorder(res) != None:
            print(printInorder(res)[:len(printInorder(res)) - 2])
        print()
# } Driver Code Ends