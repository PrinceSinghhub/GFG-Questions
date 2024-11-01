class Solution:
    def sumOfLastN_Nodes(self, head, n):
        data = []
        while head:
            data.append(head.data)
            head = head.next
        return sum(data[-n:])