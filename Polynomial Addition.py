# {
# Driver Code Starts
# Node Class
class node:
    def __init__(self, coeff, pwr):
        self.coef = coeff
        self.next = None
        self.power = pwr


# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, coeff, pwr):
        if self.head == None:
            self.head = node(coeff, pwr)
        else:
            new_node = node(coeff, pwr)
            temp = self.head
            while (temp.next):
                temp = temp.next
            temp.next = new_node


def createList(arr, n):
    lis = Linked_List()
    k = 0
    for i in range(n):
        lis.insert(arr[k], arr[k + 1])
        k += 2
    return lis.head


# } Driver Code Ends
# your task is to complete this function
'''
 class node:
    def __init__(self, coeff, pwr):
        self.coef = coeff
        self.next = None
        self.power = pwr
'''

from collections import defaultdict


class Solution:
    def addPolynomial(self, poly1, poly2):
        head = poly1
        N, M = 0, 0
        polyn = defaultdict(int)
        while head is not None:
            polyn[head.power] += head.coef
            N += 1
            head = head.next
        head = poly2
        while head is not None:
            polyn[head.power] += head.coef
            M += 1
            head = head.next
        del (poly1)
        del (poly2)
        head = None
        root = head
        length = 0
        for power in sorted(polyn, reverse=True):
            if head is None:
                head = node(polyn[power], power)
                root = head
                continue
            head.next = node(polyn[power], power)
            head = head.next
        return root


# {
# Driver Code Starts.
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        poly1 = createList(arr, n)
        n = int(input())
        arr = list(map(int, input().strip().split()))
        poly2 = createList(arr, n)
        sum = Solution().addPolynomial(poly1, poly2)
        ptr = sum
        while ptr is not None:
            print(str(ptr.coef) + 'x^' + str(ptr.power), end='')
            ptr = ptr.next
            if ptr is not None:
                print(' +', end=' ')
        print()

# Contributed by: Sagar Gupta

# } Driver Code Ends