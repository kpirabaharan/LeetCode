# 141. Linked List Cycle

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printNode(self):
        while self:
            print(self.val)
            self = self.next

    def hasCycle(self, head) -> bool:
        nodes = {}
        i = 0
        while head not in nodes:
            if head is None:
                return False
            nodes[head] = i
            i += 1
            head = head.next
        return True

    # Quicker and uses less memory
    def hasCycle2(self, head) -> bool:
        if not head:
            return False

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
