'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
'''

class Solution:
    def reverseDLL(self, head):
        node=head
        prv=None
        while node:
            nxt=node.next
            node.next=prv
            node.prev=nxt
            prv=node
            node=nxt
        return prv

