class Solution:
    def pairWiseSwap(self, head):
        if not head or not head.next:
            return head

        dummy = Node(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            first_node = head
            second_node = head.next

            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            prev = first_node
            head = first_node.next

        return dummy.next