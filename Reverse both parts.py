class Solution:
    def reverse(self, head: Optional['Node'], k: int) -> Optional['Node']:
        # code here
        def reverseNode(head):
            curr = head
            prev = None
            while curr != None:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        temp = head
        count = 1
        while count < k:
            temp = temp.next
            count += 1

        secondNode = reverseNode(temp.next)
        temp.next = None
        firstNode = reverseNode(head)

        temp = firstNode
        while temp.next != None:
            temp = temp.next
        temp.next = secondNode

        return firstNode
