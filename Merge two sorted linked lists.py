# User function Template for python3
'''
    Function to merge two sorted lists in one
    using constant space.

    Function Arguments: head_a and head_b (head reference of both the sorted lists)
    Return Type: head of the obtained list after merger.

    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }

'''


def sortedMerge(head1, head2):
    cur1 = head1
    cur2 = head2
    arr1 = []
    arr2 = []
    while cur1:
        arr1.append(cur1.data)
        cur1 = cur1.next
    while cur2:
        arr2.append(cur2.data)
        cur2 = cur2.next
    ans = arr1 + arr2
    ans.sort()

    linked = Node(ans[0])
    cur = linked
    for n in ans[1:]:
        cur.next = Node(n)
        cur = cur.next
    return linked


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
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node


# prints the elements of linked list
def printList(n):
    while n is not None:
        print(n.data, end=' ')
        n = n.next
    print()


if __name__ == '__main__':
    for _ in range(int(input())):
        n, m = map(int, input().strip().split())

        a = LinkedList()  # create a new linked list 'a'.
        b = LinkedList()  # create a new linked list 'b'.

        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))

        for x in nodes_a:
            a.append(x)

        for x in nodes_b:
            b.append(x)

        printList(sortedMerge(a.head, b.head))

# } Driver Code Ends