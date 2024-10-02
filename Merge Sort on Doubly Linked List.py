class Solution():
    def sortDoubly(self,head):
        if not head or not head.next:
            return head

        mid = self.findMiddle(head)
        mid_next = mid.next

        mid.next = None
        mid_next.prev = None

        left_sorted = self.sortDoubly(head)
        right_sorted = self.sortDoubly(mid_next)

        sorted_list = self.merge(left_sorted, right_sorted)

        return sorted_list

    def findMiddle(self, head):
        if not head:
            return head

        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right):
        dummy = Node(None)
        current = dummy

        while left and right:
            if left.data <= right.data:
                current.next = left
                left.prev = current
                left = left.next
            else:
                current.next = right
                right.prev = current
                right = right.next
            current = current.next

        if left:
            current.next = left
            left.prev = current
        if right:
            current.next = right
            right.prev = current

        merged_head = dummy.next
        if merged_head:
            merged_head.prev = None

        return merged_head