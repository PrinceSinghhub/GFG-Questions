# User function Template for python3

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
from sortedcontainers import SortedList


class Solution:
    def mergeResult(self, node1, node2):

        mul = SortedList(reverse=True)
        p1 = node1
        p2 = node2
        new_node = Node(0)
        temp = new_node

        while p1:
            mul.add(p1.data)
            p1 = p1.next

        while p2:
            mul.add(p2.data)
            p2 = p2.next

        for x in mul:
            nn = Node(x)
            temp.next = nn
            temp = temp.next

        mul.clear()
        return new_node.next


# {
# Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:
    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next


if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):

        n1, n2 = [int(x) for x in input().split()]

        arr1 = [int(x) for x in input().split()]
        ll1 = Llist()
        tail = None
        for nodeData in arr1:
            tail = ll1.insert(nodeData, tail)

        arr2 = [int(x) for x in input().split()]
        ll2 = Llist()
        tail = None
        for nodeData in arr2:
            tail = ll2.insert(nodeData, tail)

        ob = Solution()
        resHead = ob.mergeResult(ll1.head, ll2.head)
        printList(resHead)
        print()

# } Driver Code Ends