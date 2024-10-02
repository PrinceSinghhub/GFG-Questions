class Solution:
    #Function to delete a node without any reference to head pointer.
    def deleteNode(self,node):

        if node == None or node.next == None:
            return

        nextNode = node.next
        node.data = nextNode.data
        node.next = nextNode.next
        #code here
