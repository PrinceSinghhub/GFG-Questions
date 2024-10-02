class Solution:

    def subLinkedList(self, l1, l2):

        s1, s2 = '', ''
        while l1:
            s1 += str(l1.data)
            l1 = l1.next
        while l2:
            s2 += str(l2.data)
            l2 = l2.next
        num1, num2 = int(s1), int(s2)
        return Node(abs(num1 - num2))