class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head:ListNode):
    """
        Given the head of a singly linked list, 
        reverse the list, and return the reversed list. 
    """
    prev = None
    while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
    return prev

    