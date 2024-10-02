# User function Template for python3

# Linked List Node Structure

'''class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None  '''


class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize
        # next as null


# Linked List class
class LinkedList:

    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None

    def push(self, val):

        # 1 & 2: Allocate the Node &
        #        Put in the data
        new_node = Node(val)

        # 3. Make next of new Node as head
        new_node.next = self.head

        # 4. Move the head to point to new Node
        self.head = new_node

    def moveZeroes(self):
        if (self.head is None):
            return
        temp = self.head.next
        prev = self.head
        while (temp is not None):
            if (temp.data == 0):
                curr = temp
                temp = temp.next
                prev.next = temp
                curr.next = self.head
                self.head = curr
            else:
                prev = temp
                temp = temp.next
        return

    def display(self):
        temp = self.head
        while (temp is not None):
            print(temp.data, end=" ")
            temp = temp.next