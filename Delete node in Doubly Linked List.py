class Solution:
    def delete_node(self, head, x):
        l = head
        i = 1
        while head != None:
            if i == x:
                n = head.next
                p = head.prev
                if p != None:
                    p.next = n
                else:
                    l = n
                break
            i += 1
            head = head.next
        return l

#{
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    @staticmethod
    def print_list(node):
        while node is not None:
            print(node.data, end=" ")
            node = node.next
        print()


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1
    for _ in range(t):
        n = int(data[index])
        index += 1
        head = None
        tail = head

        for i in range(n):
            temp = int(data[index])
            index += 1
            if head is None:
                head = Node(temp)
                tail = head
            else:
                new_node = Node(temp)
                tail.next = new_node
                new_node.prev = tail
                tail = new_node

        x = int(data[index])
        index += 1

        obj = Solution()
        res = obj.delete_node(head, x)

        Node.print_list(res)

# } Driver Code Ends