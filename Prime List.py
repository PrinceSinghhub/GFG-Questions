from typing import Optional

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

You can also use the following for printing the link list.
printList(node)
"""


class Solution:
    def primeList(self, head: Optional['Node']) -> Optional['Node']:
        # code here
        from bisect import bisect
        mvalue = 2 * 10 ** 4
        primes = [True] * mvalue
        primes[0] = primes[1] = False
        for i in range(2, mvalue):
            if primes[i]:
                for j in range(i * i, mvalue, i):
                    primes[j] = False
        primes = [i for i, v in enumerate(primes) if v]

        t = head
        while t:
            i = bisect(primes, t.data)
            d1 = abs(primes[i - 1] - t.data)
            d2 = abs(primes[i] - t.data)
            t.data = primes[i - 1] if d1 <= d2 else primes[i]
            t = t.next
        return head


# {
# Driver Code Starts
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def printList(node):
    while (node != None):
        print(node.data, end=" ")
        node = node.next
    print()


def inputList():
    n = int(input())  # lenght of link list
    data = [int(i) for i in input().strip().split()]  # all data of linked list in a line
    head = Node(data[0])
    tail = head;
    for i in range(1, n):
        tail.next = Node(data[i]);
        tail = tail.next;
    return head;


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        head = inputList()

        obj = Solution()
        res = obj.primeList(head)

        printList(res)

# } Driver Code Ends