class Solution:
    LEFT_TURN = 0
    RIGHT_TURN = 1

    @staticmethod
    def find_common_ancestor(root, first, second):
        """
        Finds the common ancestor of given nodes.
        """
        if root is None:
            return root
        if root.data == first or root.data == second:
            # Found the target node return this node to caller
            return root
        node_found_in_left = Solution.find_common_ancestor(root.left, first, second)
        node_found_in_right = Solution.find_common_ancestor(root.right, first, second)
        if node_found_in_left and node_found_in_right:
            # Both left and right returned a node which means this node is the common ancestor
            return root
        if node_found_in_left:
            # The common ancestor was found left sub tree
            return node_found_in_left
        if node_found_in_right:
            # The common ancestor was found right right subtree
            return node_found_in_right

    @staticmethod
    def find_path(root, tgt_val, running_path, path_list):
        """
        Given a node, find the path to the target node value and
        record the path in running_path (making a copy as we go) as recursive calls are made.
        The running_path becomes the target path when the target node is found
        and is returned in the path list.
        """
        if root is None:
            return
        if root.data == tgt_val:
            # Target path found
            path_list.extend(running_path)
            return

        left_path_copy = running_path[:]
        left_path_copy.append(Solution.LEFT_TURN)
        Solution.find_path(root.left, tgt_val, left_path_copy, path_list)

        right_path_copy = running_path[:]
        right_path_copy.append(Solution.RIGHT_TURN)
        Solution.find_path(root.right, tgt_val, right_path_copy, path_list)

    def NumberOFTurns(self, root, first, second):
        if root is None:
            return 0
        if first == second:
            return 0
        # Find ancestor
        # eg:
        #          1
        #       /    \
        #       2       3
        #     /  \     /  \
        #    4    5   6    7
        #   /        / \
        #  8        9   10
        # would return 1
        ancestor = Solution.find_common_ancestor(root, first, second)

        path_to_first = []
        # Find path from ancestor to 'first'
        self.find_path(ancestor, first, [], path_to_first)
        # eg: path_to_first would have LEFT, RIGHT

        path_to_second = []
        # Find path from ancestor to second
        self.find_path(ancestor, second, [], path_to_second)
        # eg: path_to_second would have RIGHT, LEFT, RIGHT

        # Make the entire path anticlockwise so that you start from first and end up in second
        path_to_first.reverse()
        # eg: Path to first would be RIGHT, LEFT
        # Now when you combine path_to_first with the path_to_second you would have path
        # from first to second in a uniform order
        # eg: RIGHT, LEFT, RIGHT, LEFT, RIGHT
        path_to_first.extend(path_to_second)
        num_of_turns = 0
        path = path_to_first
        prev_path = path[0]
        for idx in range(1, len(path)):
            cur_path = path[idx]
            if prev_path != cur_path:
                num_of_turns += 1
            prev_path = cur_path
        return num_of_turns if num_of_turns != 0 else -1


# {
# Driver Code Starts
# Initial Template for Python 3

from collections import deque


# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        n1, n2 = list(map(int, input().strip().split()))
        ob = Solution()
        turn = ob.NumberOFTurns(root, n1, n2)
        if turn != 0:
            print(turn)
        else:
            print(-1)
# } Driver Code Ends