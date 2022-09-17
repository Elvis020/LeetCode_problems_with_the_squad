def hasCycle(head) -> bool:
    is_seen = set()
    current = head
    while current:
        if current in is_seen:
            return True
        is_seen.add(current)
        current = current.next
    return False


# Using the 2-pointer approach(fast and slow pointer, if the 2 pointer
# meet then there is a cycle
def hasCycle_II(head) -> bool:
    first_pointer = second_pointer = head
    while first_pointer and second_pointer.next:
        first_pointer = first_pointer.next
        second_pointer = second_pointer.next.next
        if first_pointer == second_pointer:
            return True
    return False
