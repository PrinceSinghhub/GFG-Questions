class Solution:
    def simple_clone(self, root):
        if root is None:
            return None
        else:
            new_root = Node(root.data)
            if root.random:
                new_root.random = Node(root.random.data)
            new_root.left = self.simple_clone(root.left)
            new_root.right = self.simple_clone(root.right)

        return new_root

    def cloneTree(self, root):
        new_root = self.simple_clone(root)

        return new_root