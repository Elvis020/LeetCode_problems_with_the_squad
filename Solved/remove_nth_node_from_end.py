def remove_nth_node_from_end(head, n):
    slow = fast = head
    for _ in range(n):
        fast = fast.next

    # When there is only 1 element
    if fast.next is None:
        return head.next

    # When there is more than one element
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return head
