class Solution:

    def reorderList(self, head):
        arr = []
        temp = head
        count = 0

        while temp is not None:
            arr.append(temp.data)
            temp = temp.next
            count += 1

        temp = head
        pos = 0
        while temp is not None:
            temp.data = arr[pos]
            if not temp.next: break
            temp.next.data = arr[count - 1 - pos]
            pos += 1
            temp = temp.next.next
        return head


# {
# Driver Code Starts
# Initial Template for Python 3

# Node Class
class node:
    def __init__(self, val):
        self.data = val
        self.next = None


# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
            self.tail = self.head
        else:
            new_node = node(val)
            self.tail.next = new_node
            self.tail = new_node

    def createList(self, arr, n):
        for i in range(n):
            self.insert(arr[i])
        return self.head

    def printList(self, head):
        tmp = head
        while tmp is not None:
            print(tmp.data, end=" ")
            tmp = tmp.next
        print()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        lis = Linked_List()
        head = lis.createList(arr, n)
        ob = Solution()
        ob.reorderList(head)

        lis.printList(head)

# } Driver Code Ends