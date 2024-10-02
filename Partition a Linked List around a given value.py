class Solution:
    def insert_to_list(self, node, list_tail):
        node.next = None
        list_tail.next = node
        return node

    def partition(self, head, x):
        # code here
        less_head = less_itr = Node(None)
        equal_head = equal_itr = Node(None)
        greater_head = greater_itr = Node(None)
        itr = head
        while itr:
            future = itr.next
            if itr.data < x:
                less_itr = self.insert_to_list(itr, less_itr)
            elif itr.data == x:
                equal_itr = self.insert_to_list(itr, equal_itr)
            else:
                greater_itr = self.insert_to_list(itr, greater_itr)
            itr = future

        less_head = less_head.next
        equal_head = equal_head.next
        greater_head = greater_head.next

        if equal_head:
            equal_itr.next = greater_head
        if less_head:
            less_itr.next = equal_head or greater_head
        head = less_head or equal_head or greater_head
        return head