from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


list1 = ListNode(val=1)
list2 = ListNode(val=2)
list3 = ListNode(val=3)
list4 = ListNode(val=4)
list1.next = list2
list2.next = list3
list3.next = list4

list5 = ListNode(val=1)
list6 = ListNode(val=6)
list7 = ListNode(val=7)
list8 = ListNode(val=8)
list5.next = list6
list6.next = list7
list7.next = list8


def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]):
    # create dummy node so we can compare the first node in each list
    result = ListNode()

    # initialise current node pointer
    dummy = result


    if not l1: return l2
    if not l2: return l1
    while l1 and l2:
        if l1.val < l2.val:
            dummy.next = l1
            l1 = l1.next
        else:
            dummy.next = l2
            l2 = l2.next
        dummy = dummy.next
    if l1:
        dummy.next = l1
    elif l2:
        dummy.next = l2

    return result.next


def printLinkedList(l):
    while l:
        print(l.val)
        l = l.next


res = mergeTwoLists(list1, list5)
printLinkedList(res)