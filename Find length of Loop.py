'''
Structure of node

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''


# Implements the Floyd's Cycle Detection Algorithm or the 'Tortoise and Hare' Algorithm
def countNodesinLoop(head):
    # If the Linked List (LL) is empty, or only contains a single item, return 0
    if ((not head) or (not head.next)):
        return 0

    tortoise = head  # The 'slow' search
    hare = head.next  # The 'fast' search

    while hare and hare.next:  # While no end of the graph is detected (because if we find one we're in an acyclic graph)
        if tortoise == hare:  # The hare and tortoise meet, a loop exists. Stop the tortoise he marks the start of the loop
            # From here, we count the nodes in the LL
            count = 1

            hare = hare.next  # Let the hare advance further

            while (
                    hare != tortoise):  # While the hare hasn't come back the tortoise, continue to count nodes and advance
                hare = hare.next
                count += 1

            return count

        tortoise = tortoise.next  # Tortoise plods along
        hare = hare.next.next  # Hare races ahead!

    # If while loop ends, no loop
    return 0


# {
#  Driver Code Starts
# Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    # connects last node to node at position pos from begining.
    def loopHere(self, pos):
        if pos == 0:
            return

        walk = self.head
        for i in range(1, pos):
            walk = walk.next

        self.tail.next = walk


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())

        LL = LinkedList()
        for i in input().split():
            LL.insert(int(i))

        LL.loopHere(int(input()))

        print(countNodesinLoop(LL.head))

# } Driver Code Ends