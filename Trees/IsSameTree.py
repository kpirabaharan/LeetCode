# 100 Same Tree


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Print the tree
    def printTree(self):
        print(self.val)
        if self.left:
            self.left.printTree()
        if self.right:
            self.right.printTree()

    def isSameTree(self, p, q) -> bool:
        # Both empty = True
        if not p and not q:
            return True
        # One empty = False
        if not p or not q:
            return False
        # Normal Case
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(
            p.right, q.right
        )


p1 = Node(1)
p2 = Node(2)
p3 = Node(3)
p1.left = p2
p1.right = p3

q1 = Node(1)
q2 = Node(2)
q3 = Node(3)
q1.left = q2
q1.right = q3

# p1.printTree()
print(p1.isSameTree(p1, q1))
