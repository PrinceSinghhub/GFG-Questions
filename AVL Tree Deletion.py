class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

def height(node):
    if node is None:
        return 0
    return node.height

def getBalanceFactor(node):
    if node is None:
        return 0
    return height(node.left) - height(node.right)

def leftRotate(root):
    new_mid = root.right
    temp = new_mid.left

    new_mid.left = root
    root.right = temp

    root.height = max(height(root.left), height(root.right)) + 1
    new_mid.height = max(height(new_mid.left), height(new_mid.right)) + 1

    return new_mid

def rightRotate(root):
    new_mid = root.left
    temp = new_mid.right

    new_mid.right = root
    root.left = temp

    root.height = max(height(root.left), height(root.right)) + 1
    new_mid.height = max(height(new_mid.left), height(new_mid.right)) + 1

    return new_mid

def successorInorder(root):
    curr = root
    while curr and curr.left is not None:
        curr = curr.left
    return curr

def deleteNode(root, data):
    if root is None:
        return root

    if data < root.data:
        root.left = deleteNode(root.left, data)
    elif data > root.data:
        root.right = deleteNode(root.right, data)
    else:
        if root.left is None and root.right is None:
            return None
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        successor = successorInorder(root.right)
        root.data = successor.data
        root.right = deleteNode(root.right, successor.data)

    if root is None:
        return root

    root.height = max(height(root.left), height(root.right)) + 1
    balance = getBalanceFactor(root)

    if balance <= 1 and balance >= -1:
        return root

    if balance > 1 and getBalanceFactor(root.left) >= 0:
        return rightRotate(root)

    if balance > 1 and getBalanceFactor(root.left) < 0:
        root.left = leftRotate(root.left)
        return rightRotate(root)

    if balance < -1 and getBalanceFactor(root.right) <= 0:
        return leftRotate(root)

    if balance < -1 and getBalanceFactor(root.right) > 0:
        root.right = rightRotate(root.right)
        return leftRotate(root)
