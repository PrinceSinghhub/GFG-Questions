def areIdentical(head1, head2):
    l1 = []
    l2 = []
    while head1:
        l1.append(head1.data)
        head1 = head1.next
    while head2:
        l2.append(head2.data)
        head2 = head2.next
    if l1 == l2:
        return True
    else:
        return False

