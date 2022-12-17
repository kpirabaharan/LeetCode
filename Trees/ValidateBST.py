# 98 - Validate Binary Search Tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isValidBST(self, root) -> bool:
        def isValid(root, left, right):
            if not root:
                return True

            if not (left < root.val < right):
                return False

            return isValid(root.left, left, root.val) and isValid(
                root.right, root.val, right
            )

        return isValid(root, float("-inf"), float("inf"))


n1 = TreeNode(5)
n2 = TreeNode(4)
n3 = TreeNode(7)
n4 = TreeNode(4)
n5 = TreeNode(8)
n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

print(n1.isValidBST(n1))
