# your task is to complete this function
# function should return an integer
'''
class node:
    def __init__(self):
        self.data = None
        self.next = Non
'''


class Solution:
    def maxPalindrome(self, head):

        def count(h1, h2):
            cnt = 0
            while h1 and h2 and h1.data == h2.data:
                cnt += 1
                h1 = h1.next
                h2 = h2.next
            return cnt

        prev = node()
        ans = 0
        while head:
            ans = max(ans, 2 * count(prev.next, head.next) + 1)
            off, head = head, head.next
            prev.next, off.next = off, prev.next
            ans = max(ans, 2 * count(prev.next, head))
        return ans


# {
# Driver Code Starts
# Node Class
class node:
    def __init__(self):
        self.data = None
        self.next = None


# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while (temp.next):
                temp = temp.next
            temp.next = new_node


# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        obj = Solution()
        print(obj.maxPalindrome(list1.head))
# Contributed By: Harshit Sidhwa

# } Driver Code Ends