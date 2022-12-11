# 572 Subtree of Another Tree

# This problem is SameTree at certain nodes


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isSubTree(self, root, subRoot) -> bool:
        # Can be at root and null but not null and subroot
        if root and not subRoot:
            return True
        if not root and subRoot:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubTree(root.left, subRoot) or self.isSubTree(
            root.right, subRoot
        )

    def isSameTree(self, p, q) -> bool:
        # Leafs
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(
                p.right, q.right
            )

        return False


n1 = TreeNode(2)
n2 = TreeNode(4)
n3 = TreeNode(6)
n4 = TreeNode(1)
n5 = TreeNode(2)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5


m1 = TreeNode(4)
m2 = TreeNode(1)
m3 = TreeNode(2)
m1.left = m2
m1.right = m3

print(n1.isSubTree(n1, m1))
print(n1.isSubTree(n2, m1))
