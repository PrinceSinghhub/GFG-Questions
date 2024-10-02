import collections


class Solution:
    def duplicateSubtreeNaryTree(self, root):
        PRIME = 1337
        hashes = collections.defaultdict(int)

        """
        hash = 1337 * (root + 1*a + 2*b + 3*c + 4*d + ....)
        """

        def dfs(r):
            nonlocal hashes
            if not r: return 1
            ret = r.key
            for i in range(len(r.children)):
                ret += (i + 1) * dfs(r.children[i])
            ret = ret * PRIME
            hashes[ret] += 1
            return ret

        dfs(root)
        ans = 0
        for k, v in hashes.items(): ans += (v > 1)
        return ans


# {
# Driver Code Starts
# Initial Template for Python 3

from collections import defaultdict
from collections import deque


class NodeNotFoundException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Node:
    def __init__(self, key, children=None):
        self.key = key
        self.children = children or []

    def __str__(self):
        return str(self.key)


class N_ary_Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def find_node(self, node, key):
        if node == None or node.key == key:
            return node
        for child in node.children:
            return_node = self.find_node(child, key)
            if return_node:
                return return_node
        return None

    def add(self, new_key, parent_key=None):
        new_node = Node(new_key)
        if parent_key == None:
            self.root = new_node
            self.size = 1
        else:
            parent_key.children.append(new_node)
            self.size += 1
        return new_node


if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):

        N = [el for el in input().split()]
        '''
        N-ary Tree Building
        '''

        tree = N_ary_Tree()
        curr = 0
        for i in range(len(N)):
            if i == 0:
                q = deque()
                curr = tree.add(int(N[0]))
            elif N[i] == " " or N == "\n":
                continue
            elif q and N[i] == "N":
                curr = q.popleft()
            elif N[i] != "N":
                q.append(tree.add(int(N[i]), curr))

        res = Solution().duplicateSubtreeNaryTree(tree.root)
        print(res)
# } Driver Code Ends