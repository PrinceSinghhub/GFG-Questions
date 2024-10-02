#User function Template for python3

class Solution:
    def modify_the_list(self, head):
        a=[]
        x=head
        while True:
            a.append(x.data)
            if(x.next==None):
                break
            x=x.next
        n= int(len(a))
        for i in range(int(n/2)):
            t=a[i]
            a[i]=a[n-i-1]-a[i]
            a[n-i-1]=t
        x=head
        i=0
        while True:
            x.data=a[i]
            i+=1
            if(x.next==None):
                pass
            x=x.next
        return head

#{
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def modify_the_list(head):
    current = head
    while current is not None:
        if current.next is not None and current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head


def print_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()


t = int(input())
while t > 0:
    n = int(input())
    linked_list_arr = list(map(int, input().split()))
    head = None
    temp = None
    for a in linked_list_arr:
        new_node = Node(a)
        if head is None:
            head = new_node
        else:
            temp.next = new_node
        temp = new_node
    head = Solution().modify_the_list(head)
    print_list(head)
    t -= 1
# } Driver Code Ends