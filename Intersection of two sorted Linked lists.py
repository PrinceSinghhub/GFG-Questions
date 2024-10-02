class Solution:
    def findIntersection(self, head1, head2):

        nodes = {}
        dummy = Node(-1)
        curr = dummy

        while head1:
            nodes[head1.data] = nodes.get(head1.data, 0) + 1
            head1 = head1.next

        while head2:
            if head2.data in nodes and nodes[head2.data] > 0:
                curr.next = Node(head2.data)
                nodes[head2.data] -= 1
                curr = curr.next
            head2 = head2.next

        return dummy.next
