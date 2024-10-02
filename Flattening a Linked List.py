# User function Template for python3


'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None

'''


class Solution():
    def merge(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        head = Node(-1)
        tmp = head
        while l1 != None and l2 != None:
            if l1.data <= l2.data:
                tmp.bottom = l1
                l1 = l1.bottom
            else:
                tmp.bottom = l2
                l2 = l2.bottom
            tmp = tmp.bottom
        if l1 != None:
            tmp.bottom = l1
        if l2 != None:
            tmp.bottom = l2
        return head.bottom

    def flatten(self, root):
        # Your code here
        while root.next != None:
            a = root
            b = root.next
            c = root.next.next
            root = self.merge(a, b)
            root.next = c
        return root


# {
# Driver Code Starts
# Initial Template for Python 3

class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None


def printList(node):
    while (node is not None):
        print(node.data, end=" ")
        node = node.bottom

    print()


if __name__ == "__main__":
    t = int(input())
    while (t > 0):
        head = None
        N = int(input())
        arr = []

        arr = [int(x) for x in input().strip().split()]
        temp = None
        tempB = None
        pre = None
        preB = None

        flag = 1
        flag1 = 1
        listo = [int(x) for x in input().strip().split()]
        it = 0
        for i in range(N):
            m = arr[i]
            m -= 1
            a1 = listo[it]
            it += 1
            temp = Node(a1)
            if flag is 1:
                head = temp
                pre = temp
                flag = 0
                flag1 = 1
            else:
                pre.next = temp
                pre = temp
                flag1 = 1

            for j in range(m):
                a = listo[it]
                it += 1
                tempB = Node(a)
                if flag1 is 1:
                    temp.bottom = tempB
                    preB = tempB
                    flag1 = 0
                else:
                    preB.bottom = tempB
                    preB = tempB
        obj = Solution()
        root = obj.flatten(head)
        printList(root)

        t -= 1

# } Driver Code Ends