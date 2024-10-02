class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        dups = set()
        dups.add(head.data)
        node = head
        while node.next:
            if node.next.data in dups:
                node.next = node.next.next
            else:
                dups.add(node.next.data)
                node = node.next
        return head
