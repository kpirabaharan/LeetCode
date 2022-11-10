# 21. Merge Two Sorted Lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printNode(self):
        while self:
            print(self.val)
            self = self.next


# Quick
def mergeTwoLists(list1, list2):
    head = ListNode()
    tail = head

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    else:
        tail.next = list2

    return head.next


def mergeTwoListsDumb(list1, list2):
    if list1 and list2:
        if list1.val <= list2.val:
            head = ListNode(list1.val)
            list1 = list1.next
        elif list2.val < list1.val:
            head = ListNode(list2.val)
            list2 = list2.next
        temp = head
    elif list1:
        head = ListNode(list1.val)
        list1 = list1.next
        temp = head
    elif list2:
        head = ListNode(list2.val)
        list2 = list2.next
        temp = head
    else:
        return None

    while list1 or list2:
        if list1:
            val1 = list1.val
        else:
            val1 = None
        if list2:
            val2 = list2.val
        else:
            val2 = None
        if val1 and val2:
            if val1 <= val2:
                nxt = ListNode(val1)
                temp.next = nxt
                list1 = list1.next
                temp = temp.next
            else:
                nxt = ListNode(val2)
                temp.next = nxt
                list2 = list2.next
                temp = temp.next
        elif val1 and val2 is None:
            nxt = ListNode(val1)
            temp.next = nxt
            list1 = list1.next
            temp = temp.next
        elif val2 and val1 is None:
            nxt = ListNode(val2)
            temp.next = nxt
            list2 = list2.next
            temp = temp.next
    return head
