class Solution:

    def insert(self, root, Key):

        if not root:
            return Node(Key)
        current = root
        while True:
            if Key < current.data:
                if current.left is None:
                    current.left = Node(Key)
                    break
                else:
                    current = current.left
            elif Key > current.data:
                if current.right is None:
                    current.right = Node(Key)
                    break
                else:
                    current = current.right
            else:
                break

        return root