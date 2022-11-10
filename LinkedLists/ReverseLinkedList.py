# 206 Reverse Linked List

# Iterative Solution using 2 Pointer Method BETTER
# T = O(n), M = O(1)
def reverseList(head):
    prev, curr = None, head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printNode(self):
        while self:
            print(self.val)
            self = self.next

    # Recursive Solution
    # T = O(n), M = O(n)
    def reverseListRecursive(self, head):
        # Base Case where list is empty
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseListRecursive(head.next)
            head.next.next = head
        head.next = None

        return newHead


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d
d.next = b
print(b)
print(d.next)
# f = reverseList(a)
# f.printNode()
