# User function Template for python3
'''
Function Arguments :
		@param  : head (given head of linked list), k(value of k)
		@return : None, Just swap the nodes

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''


def swapkthnode(head, num, k):
    # return head of new linked list
    # code here
    tail = head
    head_req = head
    tail_req = head
    tail_req_pre = None
    tail_req_next = None
    head_req_pre = None
    head_req_next = None
    if (k > num):
        return head
    m = float(k)
    if (m == (num / 2)):
        mummy(head, num, k)
        return head
    elif (m > num / 2):
        k = num - k + 1
        if (float(k) == (num / 2)):
            mummy(head, num, k)
            return head
    if (k == 1 or k == num):
        while tail.next:
            tail_req_pre = tail
            tail = tail.next

        tail_req_pre.next = head_req
        tail.next = head_req.next
        head_req.next = None
        return tail
    else:
        # print(count,"   ",head_req_pre.data,head_req.data,head_req_next.data)
        for i in range(1, num + 1):
            if (i < k):
                head_req_pre = head_req
                head_req = head_req.next
                head_req_next = head_req.next
            elif (i == k):
                tail_req_pre = head_req
                tail_req = tail_req_pre.next
                tail_req_next = tail_req.next
            elif (i <= (num - k)):
                tail_req_pre = tail_req
                tail_req = tail_req.next
                tail_req_next = tail_req.next
            else:
                break

            '''tail_req_pre = tail_req
            tail_req = tail_req.next
            tail_req_next = tail_req.next
            if()'''
        # print(tail_req_pre.data,tail_req.data,"  ",tail_req_next.data)
        head_req_pre.next = tail_req
        tail_req.next = head_req_next

        tail_req_pre.next = head_req
        head_req.next = tail_req_next
        # print(head_req_pre.next.data,tail_req_pre.next.data)
        return head


def mummy(head, num, k):
    tail = head
    head_req = head
    tail_req = head
    tail_req_next = None
    head_req_pre = None
    for i in range(1, int(num / 2)):
        head_req_pre = head_req
        head_req = head_req.next
    # print(head_req_pre.data,head_req.data)
    tail_req = head_req.next
    tail_req_next = tail_req.next
    # print(tail_req.data,tail_req_next.data)
    head_req_pre.next = tail_req
    head_req.next = tail_req_next
    tail_req.next = head_req
    # print(head.data,head.next.data,head.next.next.data,head.next.next.data)
    return


# {
#  Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node


# returns the nth node from end.
def getNthfromEnd(head, n):
    # using two pointers, similar to finding middle element
    curr_node = head
    nth_node = head

    while n:
        if n and curr_node == None:
            return None
        curr_node = curr_node.next
        n -= 1

    while curr_node:
        curr_node = curr_node.next
        nth_node = nth_node.next

    return nth_node


# returns the nth node from beg.
def getNthfromBeg(head, n):
    curr_node = head
    for i in range(n - 1):
        if curr_node is None:
            return None
        else:
            curr_node = curr_node.next

    return curr_node


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n, kth_node = map(int, input().strip().split())
        a = LinkedList()  # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list

        # intial nodes at respective positions.
        check = [getNthfromBeg(a.head, kth_node), getNthfromEnd(a.head, kth_node)]

        new_head = swapkthnode(a.head, n, kth_node)

        new_check = [getNthfromEnd(new_head, kth_node), getNthfromBeg(new_head, kth_node)]
        if (check == new_check):
            print(1)
        else:
            print(0)