class Solution:
    def insert_node(self, prev, data):
        new_node = Node(data)
        tmp = prev.next
        prev.next = new_node
        new_node.next = tmp

    def sorted_insert(self, head, data):
        if not head:
            head = Node(data)
            head.next = head
            return head

        curr = head
        while curr:
            if head.data > data:
                self.insert_node(head, data)
                head.data, head.next.data = head.next.data, head.data
                break
            if curr.next.data >= data:
                self.insert_node(curr, data)
                break
            curr = curr.next
            if curr.next == head:
                self.insert_node(curr, data)
                break

        return head