'''
# node class:

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''


class Solution:
    def sum_at_distK(self, root, target, k):
        def build_path(node, parent, path):
            if not node:
                return None

            path[node] = parent
            if node.data == target:
                return node

            return build_path(node.left, node, path) or build_path(node.right, node, path)

        def travese(n, k, visited):
            if not n or n in visited or k < 0:
                return

            nonlocal s
            visited.add(n)
            s += n.data

            travese(n.left, k - 1, visited)
            travese(n.right, k - 1, visited)

        path = {}
        start = build_path(root, None, path)
        visited = set()
        s = 0
        while start and k >= 0:
            travese(start, k, visited)
            start = path[start]
            k -= 1
        return s