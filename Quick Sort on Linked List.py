class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def getTail(node):
    while node and node.next:
        node = node.next
    return node


def partition(head, end):
    pivot = end
    prev, curr, tail = None, head, end
    new_head, new_tail = head, pivot

    while curr != pivot:
        if curr.value < pivot.value:
            if new_head is None:
                new_head = curr
            prev = curr
            curr = curr.next
        else:
            if prev:
                prev.next = curr.next
            tmp = curr.next
            curr.next = None
            new_tail.next = curr
            new_tail = curr
            curr = tmp

    if new_head is None:
        new_head = pivot

    return new_head, pivot, new_tail


def quickSortRecur(head, end):
    if not head or head == end:
        return head

    new_head, pivot, new_tail = partition(head, end)

    if new_head != pivot:
        tmp = new_head
        while tmp.next != pivot:
            tmp = tmp.next
        tmp.next = None

        new_head = quickSortRecur(new_head, tmp)

        tmp = getTail(new_head)
        tmp.next = pivot

    pivot.next = quickSortRecur(pivot.next, new_tail)

    return new_head


def quickSort(head):
    if not head or not head.next:
        return head
    return quickSortRecur(head, getTail(head))
