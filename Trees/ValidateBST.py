# 98 - Validate Binary Search Tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isValidBST(self, root) -> bool:
        def isLEFTBST(root):
            if not root.left:
                return

            isLEFTBST(root.left)
            if root.right:
                isLEFTBST(root.right)

            if root.left.val < root.val:
                return True
            else:
                return False

        def isRIGHTBST(root):
            if not root.right:
                return

            if root.left:
                isRIGHTBST(root.left)
            isRIGHTBST(root.right)

            if root.val < root.right.val:
                return True
            else:
                return False

        if not root.left and not root.right:
            return True
        elif not root.left and root.right:
            return isRIGHTBST(root)
        elif root.left and not root.right:
            return isLEFTBST(root)
        else:
            return isLEFTBST(root) and isRIGHTBST(root)


n1 = TreeNode(5)
n2 = TreeNode(4)
n3 = TreeNode(6)
n4 = TreeNode(3)
n5 = TreeNode(7)
n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

m1 = TreeNode(1)
m2 = TreeNode(1)
m1.left = m2

print(n1.isValidBST(n1))
