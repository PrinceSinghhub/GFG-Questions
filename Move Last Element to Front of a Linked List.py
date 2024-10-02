from typing import Optional

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

You can also use the following for printing the link list.
printList(node)
"""


class Solution:

    def moveToFront(self, head: Optional['Node']) -> Optional['Node']:

        # code here

        if head is None:
            return head

        if head.next is None:
            return head

        curr = head

        while curr.next.next is not None:
            curr = curr.next

        temp = curr.next

        curr.next = None

        temp.next = head

        return temp


# {
# Driver Code Starts
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def printList(node):
    while (node != None):
        print(node.data, end=" ")
        node = node.next
    print()


def inputList():
    n = int(input())  # lenght of link list
    data = [int(i) for i in input().strip().split()]  # all data of linked list in a line
    head = Node(data[0])
    tail = head;
    for i in range(1, n):
        tail.next = Node(data[i]);
        tail = tail.next;
    return head;


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        head = inputList()

        obj = Solution()
        res = obj.moveToFront(head)

        printList(res)

# } Driver Code Ends