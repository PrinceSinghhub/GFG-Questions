class Solution:
    def sortedInsert(self, head,key):
        if not head or key<=head.data:
            node=Node(key)
            node.next=head
            head=node
            return head
        temp=head
        while temp.next:
            if key<=temp.next.data:
                dup=temp.next
                temp.next=Node(key)
                temp.next.next=dup
                return head
            temp=temp.next
        temp.next=Node(key)
        return head