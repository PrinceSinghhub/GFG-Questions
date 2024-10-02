class Solution:
    def isPalindrome(self, head):
        lst = []
        while head.next!=None:
            lst.append(head.data)
            head = head.next
        lst.append(head.data)
        if lst[::1] == lst[::-1]:
            return True
        else:
            return False